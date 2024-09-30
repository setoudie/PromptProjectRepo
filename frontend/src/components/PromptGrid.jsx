import { Grid } from "@chakra-ui/react";
import PromptCard from "./PromptCard.jsx";
import PromptList from "../pure_js/fetchPrompts.js";
import {useState} from "react";

const PromptGrid = () => {
    const [prompts, setPrompts] = useState([]);
    return (
        <Grid
            gap={4}
            templateColumns={{
                base: "1fr",
                md: "repeat(2, 1fr)",
                lg: "repeat(3, 1fr)", // Ajusté pour une grille plus uniforme
            }}
        >
            {/* Je dois faire en sorte que quand j'actualise j'affiche un content
             en attendant de charger tous les prompts*/}

            {PromptList.length > 0 ? (
                PromptList.map((prompt) => (
                    <PromptCard key={prompt.id} prompt={prompt} />
                ))
            ) : (
                <p>Aucun prompt disponibles</p> // Affiche un message si aucun prompt n'est disponible
            )}
        </Grid>
    );
};

export default PromptGrid;
