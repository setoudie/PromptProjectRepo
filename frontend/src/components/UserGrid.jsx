import {Box, Image, Container, Flex, Text } from "@chakra-ui/react";

const UserGrid = () =>{
    return(
        <Container px={4} m={5} maxW={"auto"} bg={"#D9D9D9"}>

            <Flex gap={100}>
                <Flex gap={100} alignItems={"center"}>
                    <Image src='/share.png' alt='open icon' width={27} height={27}></Image>
                    <Text>Contenu du Prompt...</Text>
                </Flex>
                <Flex gap={100} alignItems={"center"} l>
                    <Text>+9</Text>
                    <Text>1275 FCFA</Text>
                    <Image src='/buy.png' alt='buy icon' width={27} height={27}></Image>
                </Flex>
            </Flex>
        </Container>
    )
}

export default UserGrid;