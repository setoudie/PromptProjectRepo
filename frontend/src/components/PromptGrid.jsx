import { Grid } from "@chakra-ui/react";
import PromptCard from "./PromptCard.jsx";
import PromptList from "../pure_js/fetchPrompts.js";

const PromptGrid = () => {
    return (
        <Grid
            gap={4}
            templateColumns={{
                base: "1fr",
                md: "repeat(2, 1fr)",
                lg: "repeat(3, 1fr)", // Ajusté pour une grille plus uniforme
            }}
        >
            {PromptList.length > 0 ? (
                PromptList.map((prompt) => (
                    <PromptCard key={prompt.id} prompt={prompt} />
                ))
            ) : (
                <p>Aucun prompt disponible</p> // Affiche un message si aucun prompt n'est disponible
            )}
        </Grid>
    );
};

export default PromptGrid;
