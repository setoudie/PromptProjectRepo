import { IconButton, useDisclosure, Button, Modal, ModalOverlay, ModalContent, ModalHeader, ModalCloseButton, ModalBody, FormControl, FormLabel, Input, ModalFooter } from '@chakra-ui/react'
import { FiShoppingCart } from "react-icons/fi";
import React from "react";

const BuyPromptModal = () => {
  const { isOpen, onOpen, onClose } = useDisclosure()
  const initialRef = React.useRef(null)
  const finalRef = React.useRef(null)
  return <>
    <IconButton  onClick={onOpen}
          icon={<FiShoppingCart />}
          variant="ghost"
          aria-label="Shopping Cart"
        />


    <Modal
        initialFocusRef={initialRef}
        finalFocusRef={finalRef}
        isOpen={isOpen}
        onClose={onClose}
    >
      <ModalOverlay/>
      <ModalContent>
        <ModalHeader>Achat Du Prompt</ModalHeader>
        <ModalCloseButton />
        <ModalBody pb={6}>
            <FormControl>
              <FormLabel>E-mail</FormLabel>
              <Input ref={initialRef} placeholder='Entrez votre addresse mail' />
            </FormControl>
        </ModalBody>

          <ModalFooter>
            <Button colorScheme='blue' mr={3}>
              Envoyer
            </Button>
            <Button onClick={onClose}>Annuler</Button>
          </ModalFooter>
      </ModalContent>
    </Modal>
  </>
}

export default BuyPromptModal