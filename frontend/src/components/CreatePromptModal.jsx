import { useDisclosure, Button, Modal, ModalOverlay, ModalContent, ModalHeader, ModalCloseButton, ModalBody, FormControl, FormLabel, Input, ModalFooter } from '@chakra-ui/react'
import {BiAddToQueue} from "react-icons/bi";
import React from "react";
const CreatePromptModal = () => {
  const { isOpen, onOpen, onClose } = useDisclosure()
  const initialRef = React.useRef(null)
  const finalRef = React.useRef(null)
  return <>
    <Button  onClick={onOpen}>
      <BiAddToQueue size={20}/>
    </Button>

    <Modal
        initialFocusRef={initialRef}
        finalFocusRef={finalRef}
        isOpen={isOpen}
        onClose={onClose}
    >
      <ModalOverlay/>
      <ModalContent>
        <ModalHeader>Create a New Prompt</ModalHeader>
        <ModalCloseButton />
        <ModalBody pb={6}>
            <FormControl>
              <FormLabel>Contenu du Prompt</FormLabel>
              <Input ref={initialRef} placeholder='Description du prompt' />
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

export default CreatePromptModal