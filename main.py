##  UNIVERSIDAD DEL VALLE DE GUATEMALA
##  INTELIGENCIA ARTIFICIAL
##  LUIS PEDRO CUÉLLAR 1822

import numpy

class AIPlayer(object):
    def __init__(self, isP1ABot = True, isP2ABot = True):
        self.p1 = 1
        self.p2 = -1
        self.is_turn_of_P1 = True
        self.is_P1_a_bot = isP1ABot
        self.is_P2_a_bot = isP2ABot

        self.current_board_state = [
            [1,     1,      1,      1,      1,       0,     0,       0,      0,      0],
            [1,     1,      1,      1,      0,       0,     0,       0,      0,      0],
            [1,     1,      1,      0,      0,       0,     0,       0,      0,      0],
            [1,     1,      0,      0,      0,       0,     0,       0,      0,      0],
            [1,     0,      0,      0,      0,       0,     0,       0,      0,      0],
            [0,     0,      0,      0,      0,       0,     0,       0,      0,     -1],
            [0,     0,      0,      0,      0,       0,     0,       0,     -1,     -1],
            [0,     0,      0,      0,      0,       0,     0,      -1,     -1,     -1],
            [0,     0,      0,      0,      0,       0,     -1,     -1,     -1,     -1],
            [0,     0,      0,      0,      0,      -1,     -1,     -1,     -1,     -1],
        ]

        self.P1_camp = []
        self.P2_camp = []

        self.build_players_camp()
        self.build_game()

    def build_game_board(self):
        print(self.current_board_state)

    
    def build_players_camp(self): 
        self.P1_camp = [
            (0, 0), (1, 0), (2, 0), (3, 0), (4, 0),
            (0, 1), (1, 1), (2, 1), (3, 1),
            (0, 2), (1, 2), (2, 2),
            (0, 3), (1, 3),
            (0, 4)
        ]

        self.P2_camp = [
                                            (9, 5),
                                    (8, 6), (9, 6),
                            (7, 7), (8, 7), (9, 7),
                    (6, 8), (7, 8), (8, 8), (9, 8),
            (5, 9), (6, 9), (7, 9), (8, 9), (9, 9)
        ]

    def next_turn(self):
        self.is_turn_of_P1 = True if self.is_turn_of_P1 == False else False
    
    def end_game(self):
        if False if (False in [self.current_board_state[i[1]][i[0]] == 1 for i in self.P2_camp]) else True:
            print("JUGADOR 1 HA GANADO")

            return True

        if False if (False in [self.current_board_state[i[1]][i[0]] == -1 for i in self.P1_camp]) else True:
            print("JUGADOR 2 HA GANADO")

            return True

        return False

    def move_players_piece(self, init_position, end_position):
        self.current_board_state[end_position[1]][end_position[0]] = 1 if self.is_turn_of_P1 == True else -1
        self.current_board_state[init_position[1]][init_position[0]] = 0

    def build_game(self):
        self.build_game_board()

        while not self.end_game():
            if self.is_turn_of_P1:
                print('JUGADOR 1')

                if self.is_P1_a_bot:
                    print('implementacion de bot')
                    init_x = 0
                    init_y = 0
                    
                    end_x = 0
                    end_y = 0
                
                else:
                    init_x = input("Ingrese la coordinadas en x de la pieza que desea mover: ")
                    init_y = input("Ingrese la coordinadas en y de la pieza que desea mover: ")

                    end_x = input("Ingrese la coordinada en x a donde desea moverse: ")
                    end_y = input("Ingrese la coordinada en x a donde desea moverse: ")
                    
            else:
                print('JUGADOR 2')

                if self.is_P2_a_bot:
                    print('implementacion de bot')
                    init_x = 0
                    init_y = 0
                    
                    end_x = 0
                    end_y = 0

                else:
                    init_x = input("Ingrese la coordinadas en x de la pieza que desea mover: ")
                    init_y = input("Ingrese la coordinadas en y de la pieza que desea mover: ")

                    end_x = input("Ingrese la coordinada en x a donde desea moverse: ")
                    end_y = input("Ingrese la coordinada en x a donde desea moverse: ")

            self.move_players_piece((int(init_x), int(init_y)), (int(end_x), int(end_y)))
            self.next_turn()
            self.build_game_board()
    
    def make_directions(self, piece_position):
        N   = (piece_position[0],       piece_position[1] - 1) 
        NW  = (piece_position[0] - 1,   piece_position[1] - 1)
        W   = (piece_position[0] - 1,   piece_position[1])
        SW  = (piece_position[0] - 1,   piece_position[1] + 1)
        S   = (piece_position[0],       piece_position[1] + 1)
        SE  = (piece_position[0] + 1,   piece_position[1] + 1)
        E   = (piece_position[0] + 1,   piece_position[1])
        NE  = (piece_position[0] + 1,   piece_position[1] - 1)
        
        N   = self.valid_direction(N)
        NW  = self.valid_direction(NW)
        W   = self.valid_direction(W)
        SW  = self.valid_direction(SW)
        S   = self.valid_direction(S)    
        SE  = self.valid_direction(SE)
        E   = self.valid_direction(E)
        NE  = self.valid_direction(NE)

        return [
                        N,
                    NW,     NE,
                W,              E,
                    SW,     SE,
                        S,
        ]

    def valid_direction(self, direction):
        if (direction[0] < 0 or direction[0] > 9) and (direction[1] < 0 or direction[1] > 9):
            return None
        
        else:
            return direction
    

    
    
AIPlayer(False, False)