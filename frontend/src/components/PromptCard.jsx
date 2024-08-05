import React from 'react';
import {
    Avatar, Card, Box, CardHeader, useColorModeValue, IconButton, HStack, Text
} from "@chakra-ui/react";
import BuyPromptModal from "./BuyPromptModal.jsx";
import { FiArrowRightCircle } from "react-icons/fi";

const PromptCard = ({ prompt }) => {
    return (
        <Card>
            <CardHeader>
                <Box
                    bg={useColorModeValue("gray.200", "gray.700")}
                    p={4}
                    borderRadius="md"
                    boxShadow="md"
                    display="flex"
                    alignItems="center"
                    justifyContent="space-between"
                >
                    <HStack spacing={4} mr={7}>
                        <Avatar bg="green.400" size="lg" />
                        <Box>
                            <Text fontWeight="bold">{prompt.owner}</Text>
                            <Text>Group ??</Text>
                            <Text>{prompt.content}</Text>
                        </Box>
                    </HStack>
                    <HStack spacing={4}>
                        <Text>{prompt.price} FCFA</Text>
                        <Text>{prompt.note} /10</Text>
                        <BuyPromptModal />
                        <HStack spacing={1}>
                            <IconButton
                                icon={<FiArrowRightCircle />}
                                variant="ghost"
                                aria-label="Voir plus"
                            />
                        </HStack>
                    </HStack>
                </Box>
            </CardHeader>
        </Card>
    );
}

export default PromptCard;
