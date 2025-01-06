import { Grid, Spinner, Text } from "@chakra-ui/react";
import PromptCard from "./PromptCard.jsx";
import { useState, useEffect } from "react";

const PromptGrid = () => {
    const [prompts, setPrompts] = useState([]); // État pour stocker les prompts
    const [loading, setLoading] = useState(true); // État pour gérer le chargement
    const [error, setError] = useState(null); // État pour gérer les erreurs

    useEffect(() => {
        const url = "http://127.0.0.1:5000/prompts/dashboard";

        const fetchPrompts = async () => {
            setLoading(true); // Indique que le chargement commence
            setError(null); // Réinitialise les erreurs
            try {
                const response = await fetch(url);
                if (!response.ok) {
                    throw new Error("Erreur réseau lors de la récupération des prompts.");
                }
                const data = await response.json();
                setPrompts(data); // Met à jour l'état avec les prompts récupérés
            } catch (err) {
                console.error("Erreur :", err);
                setError(err.message); // Stocke le message d'erreur
            } finally {
                setLoading(false); // Indique que le chargement est terminé
            }
        };

        fetchPrompts();
    }, []); // Le tableau vide signifie que l'effet est exécuté au montage seulement

    return (
        <Grid
            gap={4}
            templateColumns={{
                base: "1fr",
                md: "repeat(2, 1fr)",
                lg: "repeat(3, 1fr)",
            }}
        >
            {loading ? (
                // Affiche un indicateur de chargement
                <Spinner size="xl" color="blue.500" />
            ) : error ? (
                // Affiche un message d'erreur
                <Text fontSize="lg" color="red.500">
                    {error}
                </Text>
            ) : prompts.length > 0 ? (
                // Affiche les prompts
                prompts.map((prompt) => (
                    <PromptCard key={prompt.id} prompt={prompt} />
                ))
            ) : (
                // Message si aucun prompt n'est disponible
                <Text fontSize="lg" color="gray.500">
                    Aucun prompt disponible
                </Text>
            )}
        </Grid>
    );
};

export default PromptGrid;
