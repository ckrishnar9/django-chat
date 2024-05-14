import { AppBar, Toolbar } from "@mui/material";
import { useTheme } from "@mui/material/styles";


const PrimaryAppBar = () => {
    const theme = useTheme();
    return
        <AppBar>
            <Toolbar variant="dense" 
            sx={{height: theme.primaryAppBar.height,}}>
                Home
            </Toolbar>
        </AppBar>
    
} 

export default PrimaryAppBar;