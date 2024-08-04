// src/components/PromptDashboard.jsx

import { Text } from "@chakra-ui/react";

function PromptDashboard() {
  return (
    <Text
      fontSize="4xl"
      fontWeight="bold"
      bgGradient="linear(to-r, teal.500, green.500)"
      bgClip="text"
      textAlign="center"
      mt="10"
    >
      Prompt Dashboard
    </Text>
  );
}

export default PromptDashboard;
