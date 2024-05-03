from django.db.models import Count
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.exceptions import AuthenticationFailed, ValidationError
from rest_framework.response import Response

from .models import Server
from .schema import server_list_docs
from .serializer import ServerSerializer
from .serializer import ServerSerializer


@server_list_docs
class ServerListViewSet(viewsets.ViewSet):
    """
    A viewset for listing servers.
    """

    queryset = Server.objects.all()

    def list(self, request):
        """
        Handles GET requests to the server list endpoint, applying filtering based on query parameters.

        Args:
            request (HTTPRequest): The incoming request object.

        Returns:
            Response: An HTTP response containing a serialized list of servers.

        Raises:
            AuthenticationFailed: If the 'by_user' or 'by_serverid' query parameters are used
            without an authenticated user.
            ValidationError: If there's an invalid 'by_serverid' value or the server is not found.
        """

        category = request.query_params.get("category")
        qty = request.query_params.get("qty")
        by_user = request.query_params.get("by_user") == "true"
        by_serverid = request.query_params.get("by_serverid")
        with_num_members = request.query_params.get("with_num_members") == "true"

        # if by_user or by_serverid and not request.user.is_authenticated:
        #     raise AuthenticationFailed()

        if category:
            self.queryset = self.queryset.filter(category__name=category)

        if by_user:
            if by_user and request.user.is_authenticated:
                user_id = request.user.id
                self.queryset = self.queryset.filter(member=user_id)
            else:
                raise AuthenticationFailed()

        if qty:
            self.queryset = self.queryset[: int(qty)]

        if with_num_members:
            self.queryset = self.queryset.annotate(num_members=Count("member"))

        if by_serverid:
            
            if not request.user.is_authenticated:
                raise AuthenticationFailed()

            try:
                self.queryset = self.queryset.filter(id=by_serverid)
                if not self.queryset.exists():
                    raise ValidationError(
                        detail=f"Server not found for id {by_serverid}"
                    )
            except ValueError:
                raise ValidationError(detail="Server value error")

        serializer = ServerSerializer(
            self.queryset, many=True, context={"num_members": with_num_members}
        )
        return Response(serializer.data)
