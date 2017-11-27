interface Game {
    id: string;
    turn: Position;
    players: Player[];
    row1: Row;
    row2: Row;
    row3: Row;
    gems: GemCounts;
    nobles: Noble[];
}

interface Row {
    hidden: Card[];
    revealed: Card[];
}

interface Player {
    position: Position;
    cards: Card[];
    gems: GemCounts;
    nobles: Noble[];
    reserved: Card[];
}

interface Noble {
    cards: CardCounts;
}

interface Card {
    gems: GemCounts;
    points: number;
    color: CardColor;
}

interface GemCounts {
    Black: number;
    Blue: number;
    Green: number;
    Red: number;
    White: number;
    Yellow: number;
}

interface CardCounts {
    Black: number;
    Blue: number;
    Green: number;
    Red: number;
    White: number;
}

enum CardColor {
    Black = "Black",
    Blue = "Blue",
    Green = "Green",
    Red = "Red",
    White = "White",
}

enum Position {
    North,
    East,
    South,
    West
}
