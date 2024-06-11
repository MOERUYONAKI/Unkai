import pygame

def scan(event : pygame.event.Event, input : str, max : int = 100):
    if event.type == pygame.KEYDOWN and len(input) < max:
        if event.key == pygame.K_a:
            input += 'a'

        elif event.type == pygame.K_b:
            input += 'b'
    
        elif event.key == pygame.K_c:
            input += 'c'
            
        elif event.key == pygame.K_d:
            input += 'd'
            
        elif event.key == pygame.K_e:
            input += 'e'
            
        elif event.key == pygame.K_f:
            input += 'f'
            
        elif event.key == pygame.K_g:
            input += 'g'
            
        elif event.key == pygame.K_h:
            input += 'h'
            
        elif event.key == pygame.K_i:
            input += 'i'
            
        elif event.key == pygame.K_j:
            input += 'j'
            
        elif event.key == pygame.K_k:
            input += 'k'
            
        elif event.key == pygame.K_l:
            input += 'l'
            
        elif event.key == pygame.K_m:
            input += 'm'
            
        elif event.key == pygame.K_n:
            input += 'n'
            
        elif event.key == pygame.K_o:
            input += 'o'
            
        elif event.key == pygame.K_p:
            input += 'p'
            
        elif event.key == pygame.K_q:
            input += 'q'
            
        elif event.key == pygame.K_r:
            input += 'r'
            
        elif event.key == pygame.K_s:
            input += 's'
            
        elif event.key == pygame.K_t:
            input += 't'
            
        elif event.key == pygame.K_u:
            input += 'u'
            
        elif event.key == pygame.K_v:
            input += 'v'
            
        elif event.key == pygame.K_w:
            input += 'w'
            
        elif event.key == pygame.K_x:
            input += 'x'
            
        elif event.key == pygame.K_y:
            input += 'y'
            
        elif event.key == pygame.K_z:
            input += 'z'

        elif event.key == pygame.K_SPACE:
            input += ' '
    
        elif event.key == pygame.K_EXCLAIM:
            input += '!'
            
        elif event.key == pygame.K_QUOTEDBL:
            input += '"'
            
        elif event.key == pygame.K_HASH:
            input += '#'
            
        elif event.key == pygame.K_DOLLAR:
            input += '$'
            
        elif event.key == pygame.K_PERCENT:
            input += '%'
            
        elif event.key == pygame.K_AMPERSAND:
            input += '&'
            
        elif event.key == pygame.K_QUOTE:
            input += "'"
            
        elif event.key == pygame.K_LEFTPAREN:
            input += '('
            
        elif event.key == pygame.K_RIGHTPAREN:
            input += ')'
            
        elif event.key == pygame.K_ASTERISK:
            input += '*'
            
        elif event.key == pygame.K_PLUS:
            input += '+'
            
        elif event.key == pygame.K_COMMA:
            input += ','
            
        elif event.key == pygame.K_MINUS:
            input += '-'
            
        elif event.key == pygame.K_PERIOD:
            input += '.'
            
        elif event.key == pygame.K_SLASH:
            input += '/'
            
        elif event.key == pygame.K_COLON:
            input += ':'
            
        elif event.key == pygame.K_SEMICOLON:
            input += ';'
            
        elif event.key == pygame.K_LESS:
            input += '<'
            
        elif event.key == pygame.K_EQUALS:
            input += '='
            
        elif event.key == pygame.K_GREATER:
            input += '>'
            
        elif event.key == pygame.K_QUESTION:
            input += '?'
            
        elif event.key == pygame.K_AT:
            input += '@'
            
        elif event.key == pygame.K_LEFTBRACKET:
            input += '['
            
        elif event.key == pygame.K_BACKSLASH:
            input += '\\'
            
        elif event.key == pygame.K_RIGHTBRACKET:
            input += ']'
            
        elif event.key == pygame.K_CARET:
            input += '^'
            
        elif event.key == pygame.K_UNDERSCORE:
            input += '_'
            
        elif event.key == pygame.K_BACKQUOTE:
            input += '`'
            
        elif event.key == pygame.K_LEFTBRACE:
            input += '{'
            
        elif event.key == pygame.K_BAR:
            input += '|'
            
        elif event.key == pygame.K_RIGHTBRACE:
            input += '}'
            
        elif event.key == pygame.K_TILDE:
            input += '~'

        elif event.key == pygame.K_0:
            input += '0'
            
        elif event.key == pygame.K_1:
            input += '1'
            
        elif event.key == pygame.K_2:
            input += '2'
            
        elif event.key == pygame.K_3:
            input += '3'
            
        elif event.key == pygame.K_4:
            input += '4'
            
        elif event.key == pygame.K_5:
            input += '5'
            
        elif event.key == pygame.K_6:
            input += '6'
            
        elif event.key == pygame.K_7:
            input += '7'
            
        elif event.key == pygame.K_8:
            input += '8'
            
        elif event.key == pygame.K_9:
            input += '9'

    return input