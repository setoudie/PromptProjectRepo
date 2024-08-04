// src/components/ProfileCard.jsx

import { Box, Avatar, Text, HStack, IconButton, useColorModeValue } from "@chakra-ui/react";
import { FiShoppingCart, FiMoreHorizontal, FiArrowRightCircle } from "react-icons/fi";
import BuyPromptModal from "./BuyPromptModal.jsx";

function PromptInfo() {
  return (
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
          <Text fontWeight="bold">Prompt Owner Name</Text>
          <Text>Prompt Owner Group</Text>
          <Text>Contenu du prompt ....</Text>
        </Box>
      </HStack>
      <HStack spacing={4}>

        <Text>1275 FCFA</Text>
        <Text>+9</Text>

        <BuyPromptModal/>
        <HStack spacing={1}>
          {/*<Text>Voir plus</Text>*/}
          <IconButton
            icon={<FiArrowRightCircle />}
            variant="ghost"
            aria-label="Voir plus"
          />
        </HStack>
      </HStack>
    </Box>
  );
}

export default PromptInfo;
