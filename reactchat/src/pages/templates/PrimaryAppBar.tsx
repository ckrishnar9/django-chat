import { AppBar, Toolbar } from "@mui/material";
import { useTheme } from "@mui/material/styles";


const PrimaryAppBar = () => {
    const theme = useTheme();
    return(
        <AppBar 
        sx={{

        }}>
            <Toolbar variant="dense" 
            sx={{ 
                height: theme.primaryAppBar.height,
                minHeight: theme.primaryAppBar.height
             }}>
                Home
            </Toolbar>
        </AppBar>
    )
} 

export default PrimaryAppBar;