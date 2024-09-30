import {useState} from "react";
import { Flex, ButtonGroup, Stack, Box } from '@chakra-ui/react'
import Navbar from "./components/Navbar.jsx";
import DashboardText from "./components/DashboardText.jsx";
import PromptGrid from "./components/PromptGrid.jsx";


function App() {
    const [prompts, setPrompts] = useState([]);

    return (
    <Stack minH={"100vh"}>
        <Navbar/>
        <DashboardText/>
        {/*<UserGrid/>*/}
        <Box>
            {/*<Wrap*/}
            {/*    gap={10}*/}
            {/*    justify="center"*/}
            {/*    align="center"*/}
            {/*>*/}
            {/*    <PromptInfo/>*/}
            {/*    <PromptInfo/>*/}
            {/*    <PromptInfo/>*/}
            {/*    <PromptInfo/>*/}
            {/*    <PromptInfo/>*/}
            {/*    <PromptInfo/>*/}
            {/*</Wrap>*/}
        </Box>
        {/*<PromptGrid/>*/}
        <PromptGrid/>
    </Stack>
  )
}

export default App
