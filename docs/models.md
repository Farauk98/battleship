# Models Structure

## Player:

| Attribute | Type         | Description                                   |
| --------- | ------------ | --------------------------------------------- |
| User      | Inherited    | Inherits attributes from the User model.      |
| score     | IntegerField | The player's score (default: 0).      

## Game:

| Attribute | Type         | Description                                |
| --------- | ------------ | ------------------------------------------ |
| score    | IntegerField | The score associated with the game.       |

## Battle_grid:

| Attribute | Type | Description |
| -------- | -------- | -------- |
| game   | ForeignKey   | Reference to the related Game.  |
| x   | IntegerField   | X-coordinate of the grid.  |
| y   | IntegerField   | Y-coordinate of the grid.  |
| is_ship   | BooleanField   | Indicates whether there is a ship at this grid.  |

## Move:

| Attribute    | Type         | Description                                    |
| -----------  | ------------ | ---------------------------------------------- |
| battle_grid  | ForeignKey   | Reference to the related Battle_grid.         |
| order        | IntegerField | The order of the move within the game.  