import { createBrowserRouter, RouterProvider,Route, createRoutesFromElements } from "react-router-dom";
import Home from "./pages/Home";

const router = createBrowserRouter(
  createRoutesFromElements(
    <Route path="/" element={<Home />} />
  )
);



const App: React.FC = () => {
  return (
    <RouterProvider router={router} />
  )
}

export default App;
