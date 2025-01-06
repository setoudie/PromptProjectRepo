import {
  useDisclosure,
  Button,
  Modal,
  ModalOverlay,
  ModalContent,
  ModalHeader,
  ModalCloseButton,
  ModalBody,
  FormControl,
  FormLabel,
  Input,
  ModalFooter,
  useToast,
} from "@chakra-ui/react";
import { BiAddToQueue } from "react-icons/bi";
import React, { useState } from "react";

const CreatePromptModal = () => {
  const { isOpen, onOpen, onClose } = useDisclosure();
  const initialRef = React.useRef(null);
  const finalRef = React.useRef(null);
  const [promptContent, setPromptContent] = useState(""); // État pour stocker le contenu du prompt
  const toast = useToast(); // Toast pour afficher des notifications

  // Récupération de l'URL depuis les variables d'environnement
  const promptUrl = "https://prompt-management.onrender.com/prompts/create";
;

  // Fonction pour envoyer les données au backend
  const handleSubmit = async () => {
    const data = {
      content: promptContent, // Payload à envoyer
    };

    try {
      const response = await fetch(promptUrl, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(data),
      });

      if (response.ok) {
        // Succès : afficher une notification
        toast({
          title: "Prompt créé avec succès.",
          status: "success",
          duration: 3000,
          isClosable: true,
        });
        setPromptContent(""); // Réinitialiser le formulaire
        onClose(); // Fermer la modal
      } else {
        // Erreur du serveur : afficher une notification
        const errorData = await response.json();
        toast({
          title: "Erreur lors de la création du prompt.",
          description: errorData.message || "Une erreur est survenue.",
          status: "error",
          duration: 3000,
          isClosable: true,
        });
      }
    } catch (error) {
      // Erreur de réseau ou autre
      console.error("Erreur :", error);
      toast({
        title: "Erreur de réseau.",
        description: "Vérifiez votre connexion ou contactez l'administrateur.",
        status: "error",
        duration: 3000,
        isClosable: true,
      });
    }
  };

  return (
    <>
      <Button onClick={onOpen}>
        <BiAddToQueue size={20} />
      </Button>

      <Modal
        initialFocusRef={initialRef}
        finalFocusRef={finalRef}
        isOpen={isOpen}
        onClose={onClose}
      >
        <ModalOverlay />
        <ModalContent>
          <ModalHeader>Créer un nouveau Prompt</ModalHeader>
          <ModalCloseButton />
          <ModalBody pb={6}>
            <FormControl>
              <FormLabel>Contenu du Prompt</FormLabel>
              <Input
                ref={initialRef}
                placeholder="Description du prompt"
                value={promptContent} // Liaison avec l'état
                onChange={(e) => setPromptContent(e.target.value)} // Mise à jour de l'état
              />
            </FormControl>
          </ModalBody>

          <ModalFooter>
            <Button colorScheme="blue" mr={3} onClick={handleSubmit}>
              Envoyer
            </Button>
            <Button onClick={onClose}>Annuler</Button>
          </ModalFooter>
        </ModalContent>
      </Modal>
    </>
  );
};

export default CreatePromptModal;
