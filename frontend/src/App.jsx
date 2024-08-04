import {useState} from "react";
import { Button, ButtonGroup, Stack, Container } from '@chakra-ui/react'
import Navbar from "./components/Navbar.jsx";
import UserGrid from "./components/UserGrid.jsx";
import DashboardText from "./components/DashboardText.jsx";
import CreateUserModal from "./components/CreateUserModal.jsx";

function App() {
  const [count, setCount] = useState(0)

  return (
    <Stack minH={"100vh"}>
        <Navbar/>
        <DashboardText/>
        <UserGrid/>

    </Stack>
  )
}

export default App
