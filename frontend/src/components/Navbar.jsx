import {Button, Box, Image, useColorMode, useColorModeValue, Container,Input, Flex, Text } from "@chakra-ui/react";
import { IoMoonSharp } from "react-icons/io5";
import { LuSunMedium } from "react-icons/lu";
import { RiUserSharedFill } from "react-icons/ri";
import CreatePromptModal from "./CreatePromptModal.jsx";

const Navbar = () =>{
    const { colorMode, toggleColorMode } = useColorMode()
    return (
        <Box px={4} m={4} w={"auto"} h={"70px"} bg={useColorModeValue("blue.200", "blue.700")} borderRadius={30}>
            <Flex gap={10} alignItems={"center"} justifyContent={"space-between"}>

                <Flex m={4} gap={10}>
                    <Text m={3}>Prompt Project</Text>
                    <Button onClick={toggleColorMode}>
                        {colorMode === 'light' ? <IoMoonSharp /> : <LuSunMedium size={20}/>}
                    </Button>
                </Flex>

                <Box m={4} ml={70}>
                    <Input placeholder='Recherchez un Prompt' />
                </Box>

                <Flex m={2}>
                    <CreatePromptModal/>
                    <RiUserSharedFill size={55}/>
                </Flex>
            </Flex>
        </Box>
    )
}

export default Navbar;