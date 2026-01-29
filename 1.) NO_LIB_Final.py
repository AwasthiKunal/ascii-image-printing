
rows = 39
cols = 75

for r in range(rows):
    line = ""
    for c in range(cols):
        ch = " "
        
        # Row 0
        if r == 0:
            if c >= 34 and c <= 39:
                ch = "."
            else:
                ch = "."
        
        # Row 1
        elif r == 1:
            if c >= 33 and c <= 35:
                ch = "."
            elif c >= 36 and c <= 40:
                ch = ":"
            elif c >= 41 and c <= 42:
                ch = "."
            else:
                ch = "."
        
        # Row 2
        elif r == 2:
            if c >= 33 and c <= 34:
                ch = "."
            elif c >= 35 and c <= 36:
                ch = ":"
            elif c >= 37 and c <= 42:
                ch = "-"
            elif c == 43:
                ch = ":"
            elif c == 44:
                ch = "."
            else:
                ch = "."
        
        # Row 3
        elif r == 3:
            if c >= 32 and c <= 34:
                ch = "."
            elif c >= 35 and c <= 36:
                ch = ":"
            elif c >= 37 and c <= 44:
                ch = "-"
            elif c == 45:
                ch = "."
            else:
                ch = "."
        
        # Row 4
        elif r == 4:
            if c >= 30 and c <= 33:
                ch = "."
            elif c >= 34 and c <= 35:
                ch = ":"
            elif c >= 36 and c <= 37:
                ch = "-"
            elif c >= 38 and c <= 45:
                ch = "="
            elif c == 46:
                ch = ":"
            else:
                ch = "."
        
        # Row 5
        elif r == 5:
            if c >= 18 and c <= 33:
                ch = "."
            elif c >= 34 and c <= 35:
                ch = ":"
            elif c >= 36 and c <= 37:
                ch = "-"
            elif c == 38:
                ch = "+"
            elif c >= 39 and c <= 43:
                ch = "*"
            elif c >= 44 and c <= 45:
                ch = "#"
            elif c == 46:
                ch = "*"
            elif c == 47:
                ch = ":"
            elif c == 48:
                ch = "."
            else:
                ch = "."
        
        # Row 6
        elif r == 6:
            if c >= 18 and c <= 34:
                ch = "."
            elif c >= 35 and c <= 36:
                ch = ":"
            elif c == 37:
                ch = "-"
            elif c == 38:
                ch = "="
            elif c >= 39 and c <= 46:
                ch = "*"
            elif c == 47:
                ch = "+"
            elif c == 48:
                ch = "="
            elif c >= 49 and c <= 50:
                ch = "-"
            elif c >= 51 and c <= 56:
                ch = "="
            elif c == 57:
                ch = "-"
            elif c == 58:
                ch = ":"
            elif c == 59:
                ch = "."
            else:
                ch = "."
        
        # Row 7
        elif r == 7:
            if c >= 17 and c <= 35:
                ch = "."
            elif c >= 36 and c <= 37:
                ch = ":"
            elif c == 38:
                ch = "-"
            elif c >= 39 and c <= 40:
                ch = "="
            elif c >= 41 and c <= 42:
                ch = "+"
            elif c == 43:
                ch = "*"
            elif c >= 44 and c <= 58:
                ch = "#"
            elif c == 59:
                ch = "*"
            elif c == 60:
                ch = ":"
            else:
                ch = "."
        
        # Row 8
        elif r == 8:
            if c >= 0 and c <= 4:
                ch = "."
            elif c >= 5 and c <= 16:
                ch = "."
            elif c >= 17 and c <= 32:
                ch = "."
            elif c == 33:
                ch = ":"
            elif c == 34:
                ch = "="
            elif c >= 35 and c <= 36:
                ch = "+"
            elif c == 37:
                ch = "*"
            elif c >= 38 and c <= 41:
                ch = "#"
            elif c >= 42 and c <= 53:
                ch = "%"
            elif c >= 54 and c <= 59:
                ch = "#"
            elif c == 60:
                ch = "-"
            elif c == 61:
                ch = "."
            else:
                ch = "."
        
        # Row 9
        elif r == 9:
            if c >= 0 and c <= 6:
                ch = "."
            elif c == 7:
                ch = "."
            elif c >= 8 and c <= 9:
                ch = "."
            elif c >= 10 and c <= 16:
                ch = "."
            elif c >= 17 and c <= 19:
                ch = "."
            elif c == 20:
                ch = "."
            elif c >= 21 and c <= 25:
                ch = "."
            elif c >= 26 and c <= 27:
                ch = ":"
            elif c >= 28 and c <= 29:
                ch = "-"
            elif c == 30:
                ch = "="
            elif c == 31:
                ch = "+"
            elif c >= 32 and c <= 33:
                ch = "#"
            elif c >= 34 and c <= 38:
                ch = "%"
            elif c == 39:
                ch = "#"
            elif c >= 40 and c <= 54:
                ch = "%"
            elif c >= 55 and c <= 58:
                ch = "#"
            elif c == 59:
                ch = "="
            elif c >= 60 and c <= 63:
                ch = "."
            else:
                ch = "."
        
        # Row 10
        elif r == 10:
            if c >= 0 and c <= 9:
                ch = "."
            elif c >= 10 and c <= 12:
                ch = "."
            elif c >= 13 and c <= 15:
                ch = "."
            elif c >= 16 and c <= 17:
                ch = ":"
            elif c >= 18 and c <= 19:
                ch = "-"
            elif c >= 20 and c <= 21:
                ch = "="
            elif c >= 22 and c <= 23:
                ch = "+"
            elif c >= 24 and c <= 28:
                ch = "*"
            elif c >= 29 and c <= 32:
                ch = "#"
            elif c >= 33 and c <= 36:
                ch = "%"
            elif c >= 37 and c <= 44:
                ch = "#"
            elif c >= 45 and c <= 55:
                ch = "%"
            elif c >= 56 and c <= 57:
                ch = "#"
            elif c == 58:
                ch = "+"
            elif c == 59:
                ch = "-"
            elif c >= 60 and c <= 63:
                ch = "."
            else:
                ch = "."
        
        # Row 11
        elif r == 11:
            if c >= 0 and c <= 9:
                ch = "."
            elif c == 10:
                ch = ":"
            elif c == 11:
                ch = "-"
            elif c == 12:
                ch = "="
            elif c == 13:
                ch = "+"
            elif c >= 14 and c <= 15:
                ch = "*"
            elif c >= 16 and c <= 17:
                ch = "#"
            elif c >= 18 and c <= 20:
                ch = "%"
            elif c >= 21 and c <= 22:
                ch = "#"
            elif c >= 23 and c <= 25:
                ch = "%"
            elif c >= 26 and c <= 27:
                ch = "#"
            elif c >= 28 and c <= 29:
                ch = "*"
            elif c == 30:
                ch = "+"
            elif c == 31:
                ch = "="
            elif c >= 32 and c <= 33:
                ch = "-"
            elif c >= 34 and c <= 37:
                ch = "="
            elif c == 38:
                ch = "+"
            elif c == 39:
                ch = "*"
            elif c >= 40 and c <= 41:
                ch = "#"
            elif c >= 42 and c <= 52:
                ch = "%"
            elif c == 53:
                ch = "*"
            elif c == 54:
                ch = "-"
            elif c >= 55 and c <= 58:
                ch = "."
            else:
                ch = "."
        
        # Row 12
        elif r == 12:
            if c >= 0 and c <= 7:
                ch = "."
            elif c == 8:
                ch = "-"
            elif c == 9:
                ch = "+"
            elif c == 10:
                ch = "*"
            elif c >= 11 and c <= 12:
                ch = "#"
            elif c >= 13 and c <= 19:
                ch = "%"
            elif c == 20:
                ch = "+"
            elif c >= 21 and c <= 22:
                ch = "="
            elif c >= 23 and c <= 24:
                ch = "-"
            elif c >= 25 and c <= 26:
                ch = ":"
            elif c == 27:
                ch = "-"
            elif c == 28:
                ch = "="
            elif c >= 29 and c <= 30:
                ch = "+"
            elif c == 31:
                ch = "-"
            elif c == 32:
                ch = ":"
            elif c >= 33 and c <= 34:
                ch = "."
            elif c == 35:
                ch = ":"
            elif c == 36:
                ch = "-"
            elif c == 37:
                ch = "+"
            elif c == 38:
                ch = "#"
            elif c == 39:
                ch = "%"
            elif c == 40:
                ch = "#"
            elif c == 41:
                ch = "*"
            elif c == 42:
                ch = "+"
            elif c >= 43 and c <= 44:
                ch = "="
            elif c == 45:
                ch = "+"
            elif c >= 46 and c <= 47:
                ch = "#"
            elif c >= 48 and c <= 52:
                ch = "%"
            elif c == 53:
                ch = "+"
            elif c == 54:
                ch = "-"
            elif c == 55:
                ch = ":"
            elif c >= 56 and c <= 58:
                ch = "."
            else:
                ch = "."
        
        # Row 13
        elif r == 13:
            if c >= 0 and c <= 5:
                ch = "."
            elif c == 6:
                ch = ":"
            elif c == 7:
                ch = "+"
            elif c >= 8 and c <= 11:
                ch = "#"
            elif c >= 12 and c <= 18:
                ch = "%"
            elif c == 19:
                ch = "#"
            elif c >= 20 and c <= 21:
                ch = ":"
            elif c >= 22 and c <= 24:
                ch = "."
            elif c == 25:
                ch = ":"
            elif c >= 26 and c <= 27:
                ch = "-"
            elif c >= 28 and c <= 29:
                ch = "#"
            elif c == 30:
                ch = "*"
            elif c == 31:
                ch = "-"
            elif c >= 32 and c <= 34:
                ch = "."
            elif c == 35:
                ch = ":"
            elif c == 36:
                ch = "+"
            elif c == 37:
                ch = "#"
            elif c == 38:
                ch = "%"
            elif c >= 39 and c <= 41:
                ch = "#"
            elif c >= 42 and c <= 44:
                ch = "*"
            elif c == 45:
                ch = "+"
            elif c == 46:
                ch = "="
            elif c == 47:
                ch = "+"
            elif c == 48:
                ch = "*"
            elif c >= 49 and c <= 51:
                ch = "%"
            elif c == 52:
                ch = "*"
            elif c >= 53 and c <= 58:
                ch = "."
            else:
                ch = "."
        
        # Row 14
        elif r == 14:
            if c >= 0 and c <= 5:
                ch = "."
            elif c == 6:
                ch = ":"
            elif c == 7:
                ch = "#"
            elif c >= 8 and c <= 9:
                ch = "%"
            elif c >= 10 and c <= 11:
                ch = "#"
            elif c >= 12 and c <= 15:
                ch = "%"
            elif c == 16:
                ch = "*"
            elif c == 17:
                ch = "+"
            elif c == 18:
                ch = "*"
            elif c == 19:
                ch = "="
            elif c >= 20 and c <= 24:
                ch = "."
            elif c >= 25 and c <= 27:
                ch = ":"
            elif c >= 28 and c <= 30:
                ch = "-"
            elif c == 31:
                ch = ":"
            elif c >= 32 and c <= 34:
                ch = "."
            elif c == 35:
                ch = ":"
            elif c == 36:
                ch = "="
            elif c == 37:
                ch = "*"
            elif c >= 38 and c <= 39:
                ch = "#"
            elif c >= 40 and c <= 41:
                ch = "*"
            elif c >= 42 and c <= 44:
                ch = "+"
            elif c == 45:
                ch = "="
            elif c == 46:
                ch = "-"
            elif c == 47:
                ch = "="
            elif c >= 48 and c <= 50:
                ch = "#"
            elif c == 51:
                ch = "+"
            elif c >= 52 and c <= 54:
                ch = "."
            else:
                ch = "."
        
        # Row 15
        elif r == 15:
            if c >= 0 and c <= 6:
                ch = "."
            elif c == 7:
                ch = "-"
            elif c == 8:
                ch = "*"
            elif c >= 9 and c <= 15:
                ch = "%"
            elif c == 16:
                ch = "="
            elif c >= 17 and c <= 19:
                ch = ":"
            elif c >= 20 and c <= 35:
                ch = "."
            elif c == 36:
                ch = "-"
            elif c >= 37 and c <= 39:
                ch = "="
            elif c >= 40 and c <= 41:
                ch = "-"
            elif c >= 42 and c <= 45:
                ch = ":"
            elif c >= 46 and c <= 48:
                ch = "-"
            elif c == 49:
                ch = "+"
            elif c == 50:
                ch = "="
            elif c == 51:
                ch = "*"
            elif c == 52:
                ch = "="
            elif c >= 53 and c <= 55:
                ch = "."
            else:
                ch = "."
        
        # Row 16
        elif r == 16:
            if c >= 0 and c <= 8:
                ch = "."
            elif c == 9:
                ch = "-"
            elif c == 10:
                ch = "="
            elif c == 11:
                ch = "+"
            elif c >= 12 and c <= 15:
                ch = "*"
            elif c == 16:
                ch = "="
            elif c == 17:
                ch = ":"
            elif c == 18:
                ch = "="
            elif c == 19:
                ch = ":"
            elif c >= 20 and c <= 35:
                ch = "."
            elif c == 36:
                ch = ":"
            elif c == 37:
                ch = "-"
            elif c >= 38 and c <= 40:
                ch = "="
            elif c >= 41 and c <= 42:
                ch = "-"
            elif c >= 43 and c <= 46:
                ch = ":"
            elif c >= 47 and c <= 48:
                ch = "-"
            elif c >= 49 and c <= 50:
                ch = "*"
            elif c == 51:
                ch = "+"
            elif c >= 52 and c <= 54:
                ch = "."
            elif c >= 55 and c <= 67:
                ch = "."
            elif c >= 68 and c <= 69:
                ch = "."
            elif c == 70:
                ch = "."
            else:
                ch = "."
        
        # Row 17
        elif r == 17:
            if c >= 0 and c <= 17:
                ch = "."
            elif c == 18:
                ch = ":"
            elif c >= 19 and c <= 31:
                ch = "."
            elif c == 32:
                ch = ":"
            elif c == 33:
                ch = "-"
            elif c >= 34 and c <= 35:
                ch = "."
            elif c == 36:
                ch = "-"
            elif c == 37:
                ch = "+"
            elif c == 38:
                ch = "*"
            elif c >= 39 and c <= 40:
                ch = "="
            elif c >= 41 and c <= 44:
                ch = "-"
            elif c >= 45 and c <= 46:
                ch = ":"
            elif c >= 47 and c <= 48:
                ch = "-"
            elif c == 49:
                ch = "="
            elif c == 50:
                ch = "*"
            elif c == 51:
                ch = "+"
            elif c >= 52 and c <= 55:
                ch = "."
            elif c >= 56 and c <= 63:
                ch = "."
            elif c >= 64 and c <= 70:
                ch = "."
            else:
                ch = "."
        
        # Row 18
        elif r == 18:
            if c >= 0 and c <= 29:
                ch = "."
            elif c >= 30 and c <= 31:
                ch = ":"
            elif c == 32:
                ch = "-"
            elif c == 33:
                ch = ":"
            elif c == 34:
                ch = "-"
            elif c == 35:
                ch = "+"
            elif c >= 36 and c <= 37:
                ch = "#"
            elif c == 38:
                ch = "+"
            elif c == 39:
                ch = "="
            elif c >= 40 and c <= 47:
                ch = "-"
            elif c >= 48 and c <= 49:
                ch = "="
            elif c >= 50 and c <= 55:
                ch = "."
            elif c >= 56 and c <= 60:
                ch = "."
            elif c >= 61 and c <= 70:
                ch = "."
            else:
                ch = "."
        
        # Row 19
        elif r == 19:
            if c >= 0 and c <= 27:
                ch = "."
            elif c == 28:
                ch = ":"
            elif c >= 29 and c <= 35:
                ch = "-"
            elif c == 36:
                ch = "*"
            elif c == 37:
                ch = "#"
            elif c == 38:
                ch = "%"
            elif c == 39:
                ch = "#"
            elif c == 40:
                ch = "*"
            elif c == 41:
                ch = "+"
            elif c == 42:
                ch = "="
            elif c >= 43 and c <= 47:
                ch = "-"
            elif c == 48:
                ch = "="
            elif c == 49:
                ch = ":"
            elif c >= 50 and c <= 69:
                ch = "."
            else:
                ch = "."
        
        # Row 20
        elif r == 20:
            if c >= 0 and c <= 27:
                ch = "."
            elif c >= 28 and c <= 30:
                ch = ":"
            elif c >= 31 and c <= 33:
                ch = "."
            elif c == 34:
                ch = ":"
            elif c == 35:
                ch = "="
            elif c == 36:
                ch = "+"
            elif c == 37:
                ch = "*"
            elif c == 38:
                ch = "#"
            elif c == 39:
                ch = "*"
            elif c == 40:
                ch = "+"
            elif c >= 41 and c <= 46:
                ch = "="
            elif c == 47:
                ch = ":"
            elif c >= 48 and c <= 65:
                ch = "."
            elif c == 66:
                ch = "."
            elif c >= 67 and c <= 69:
                ch = "."
            else:
                ch = "."
        
        # Row 21
        elif r == 21:
            if c >= 0 and c <= 32:
                ch = "."
            elif c >= 33 and c <= 35:
                ch = ":"
            elif c >= 36 and c <= 37:
                ch = "-"
            elif c >= 38 and c <= 39:
                ch = "="
            elif c >= 40 and c <= 41:
                ch = "-"
            elif c >= 42 and c <= 44:
                ch = "="
            elif c == 45:
                ch = "+"
            elif c == 46:
                ch = "-"
            elif c >= 47 and c <= 64:
                ch = "."
            elif c >= 65 and c <= 66:
                ch = "."
            elif c == 67:
                ch = "."
            else:
                ch = "."
        
        # Row 22
        elif r == 22:
            if c >= 0 and c <= 31:
                ch = "."
            elif c >= 32 and c <= 35:
                ch = ":"
            elif c >= 36 and c <= 40:
                ch = "-"
            elif c == 41:
                ch = "="
            elif c >= 42 and c <= 45:
                ch = "+"
            elif c == 46:
                ch = "-"
            elif c >= 47 and c <= 61:
                ch = "."
            else:
                ch = "."
        
        # Row 23
        elif r == 23:
            if c >= 0 and c <= 34:
                ch = "."
            elif c >= 35 and c <= 37:
                ch = ":"
            elif c == 38:
                ch = "-"
            elif c == 39:
                ch = "="
            elif c == 40:
                ch = "+"
            elif c >= 41 and c <= 45:
                ch = "*"
            elif c == 46:
                ch = "="
            elif c >= 47 and c <= 59:
                ch = "."
            else:
                ch = "."
        
        # Row 24
        elif r == 24:
            if c >= 0 and c <= 21:
                ch = "."
            elif c == 22:
                ch = "-"
            elif c >= 23 and c <= 30:
                ch = "."
            elif c >= 31 and c <= 33:
                ch = ":"
            elif c >= 34 and c <= 35:
                ch = "-"
            elif c == 36:
                ch = "="
            elif c >= 37 and c <= 38:
                ch = "+"
            elif c >= 39 and c <= 44:
                ch = "*"
            elif c == 45:
                ch = "+"
            elif c >= 46 and c <= 48:
                ch = "*"
            elif c == 49:
                ch = "+"
            elif c == 50:
                ch = ":"
            elif c >= 51 and c <= 57:
                ch = "."
            else:
                ch = "."
        
        # Row 25
        elif r == 25:
            if c >= 0 and c <= 20:
                ch = "."
            elif c == 21:
                ch = "-"
            elif c == 22:
                ch = "*"
            elif c == 23:
                ch = ":"
            elif c >= 24 and c <= 31:
                ch = "."
            elif c >= 32 and c <= 33:
                ch = ":"
            elif c == 34:
                ch = "-"
            elif c == 35:
                ch = "+"
            elif c >= 36 and c <= 38:
                ch = "*"
            elif c == 39:
                ch = "#"
            elif c >= 40 and c <= 42:
                ch = "*"
            elif c >= 43 and c <= 46:
                ch = "+"
            elif c == 47:
                ch = "*"
            elif c == 48:
                ch = "#"
            elif c >= 49 and c <= 50:
                ch = "%"
            elif c == 51:
                ch = "+"
            elif c == 52:
                ch = ":"
            elif c >= 53 and c <= 59:
                ch = "."
            else:
                ch = "."
        
        # Row 26
        elif r == 26:
            if c >= 0 and c <= 21:
                ch = "."
            elif c == 22:
                ch = "+"
            elif c == 23:
                ch = "-"
            elif c >= 24 and c <= 32:
                ch = "."
            elif c == 33:
                ch = ":"
            elif c == 34:
                ch = "-"
            elif c >= 35 and c <= 36:
                ch = "+"
            elif c >= 37 and c <= 39:
                ch = "*"
            elif c >= 40 and c <= 45:
                ch = "+"
            elif c == 46:
                ch = "*"
            elif c == 47:
                ch = "#"
            elif c == 48:
                ch = "%"
            elif c == 49:
                ch = "*"
            elif c == 50:
                ch = "="
            elif c == 51:
                ch = "-"
            elif c == 52:
                ch = ":"
            elif c >= 53 and c <= 57:
                ch = "."
            else:
                ch = "."
        
        # Row 27
        elif r == 27:
            if c >= 0 and c <= 22:
                ch = "."
            elif c == 23:
                ch = "+"
            elif c == 24:
                ch = "-"
            elif c >= 25 and c <= 32:
                ch = "."
            elif c >= 33 and c <= 34:
                ch = ":"
            elif c == 35:
                ch = "-"
            elif c >= 36 and c <= 41:
                ch = "="
            elif c >= 42 and c <= 45:
                ch = "+"
            elif c == 46:
                ch = "*"
            elif c == 47:
                ch = "#"
            elif c == 48:
                ch = "+"
            elif c >= 49 and c <= 50:
                ch = "="
            elif c >= 51 and c <= 52:
                ch = "-"
            elif c == 53:
                ch = ":"
            elif c >= 54 and c <= 56:
                ch = "."
            else:
                ch = "."
        
        # Row 28
        elif r == 28:
            if c >= 0 and c <= 23:
                ch = "."
            elif c >= 24 and c <= 25:
                ch = "="
            elif c == 26:
                ch = ":"
            elif c >= 27 and c <= 33:
                ch = "."
            elif c >= 34 and c <= 36:
                ch = ":"
            elif c == 37:
                ch = "-"
            elif c == 38:
                ch = ":"
            elif c == 39:
                ch = "-"
            elif c == 40:
                ch = "="
            elif c >= 41 and c <= 42:
                ch = "+"
            elif c == 43:
                ch = "="
            elif c == 44:
                ch = "+"
            elif c == 45:
                ch = "*"
            elif c == 46:
                ch = "-"
            elif c == 47:
                ch = "."
            elif c >= 48 and c <= 49:
                ch = ":"
            elif c >= 50 and c <= 52:
                ch = "-"
            elif c >= 53 and c <= 54:
                ch = "="
            elif c == 55:
                ch = "-"
            elif c == 56:
                ch = "."
            else:
                ch = "."
        
        # Row 29
        elif r == 29:
            if c >= 0 and c <= 22:
                ch = "."
            elif c == 23:
                ch = "-"
            elif c == 24:
                ch = "="
            elif c == 25:
                ch = "-"
            elif c >= 26 and c <= 27:
                ch = ":"
            elif c >= 28 and c <= 32:
                ch = "."
            elif c >= 33 and c <= 36:
                ch = ":"
            elif c >= 37 and c <= 38:
                ch = "."
            elif c == 39:
                ch = ":"
            elif c == 40:
                ch = "="
            elif c >= 41 and c <= 42:
                ch = "+"
            elif c >= 43 and c <= 45:
                ch = "-"
            elif c >= 46 and c <= 47:
                ch = ":"
            elif c == 48:
                ch = "-"
            elif c >= 49 and c <= 50:
                ch = "="
            elif c >= 51 and c <= 53:
                ch = "-"
            elif c == 54:
                ch = "+"
            elif c == 55:
                ch = "*"
            elif c == 56:
                ch = "-"
            elif c >= 57 and c <= 58:
                ch = "."
            else:
                ch = "."
        
        # Row 30
        elif r == 30:
            if c >= 0 and c <= 20:
                ch = "."
            elif c == 21:
                ch = ":"
            elif c == 22:
                ch = "+"
            elif c >= 23 and c <= 24:
                ch = "#"
            elif c == 25:
                ch = "="
            elif c == 26:
                ch = "."
            elif c >= 27 and c <= 28:
                ch = ":"
            elif c == 29:
                ch = "."
            elif c >= 30 and c <= 33:
                ch = ":"
            elif c == 34:
                ch = "-"
            elif c == 35:
                ch = ":"
            elif c >= 36 and c <= 38:
                ch = "."
            elif c == 39:
                ch = "-"
            elif c >= 40 and c <= 41:
                ch = "+"
            elif c == 42:
                ch = "-"
            elif c >= 43 and c <= 44:
                ch = ":"
            elif c == 45:
                ch = "="
            elif c == 46:
                ch = "+"
            elif c >= 47 and c <= 50:
                ch = "#"
            elif c == 51:
                ch = "*"
            elif c >= 52 and c <= 53:
                ch = "="
            elif c == 54:
                ch = "+"
            elif c == 55:
                ch = "*"
            elif c == 56:
                ch = "-"
            elif c == 57:
                ch = ":"
            elif c == 58:
                ch = "."
            elif c >= 59 and c <= 62:
                ch = ":"
            elif c >= 63 and c <= 64:
                ch = "."
            else:
                ch = "."
        
        # Row 31
        elif r == 31:
            if c >= 0 and c <= 18:
                ch = "."
            elif c == 19:
                ch = ":"
            elif c == 20:
                ch = "-"
            elif c == 21:
                ch = "+"
            elif c == 22:
                ch = "#"
            elif c == 23:
                ch = "*"
            elif c == 24:
                ch = "-"
            elif c >= 25 and c <= 26:
                ch = ":"
            elif c >= 27 and c <= 32:
                ch = "."
            elif c >= 33 and c <= 34:
                ch = ":"
            elif c == 35:
                ch = "-"
            elif c == 36:
                ch = ":"
            elif c >= 37 and c <= 39:
                ch = "."
            elif c >= 40 and c <= 41:
                ch = "-"
            elif c == 42:
                ch = ":"
            elif c == 43:
                ch = ":"
            elif c == 44:
                ch = "-"
            elif c == 45:
                ch = "*"
            elif c == 46:
                ch = "#"
            elif c == 47:
                ch = "*"
            elif c >= 48 and c <= 49:
                ch = "+"
            elif c >= 50 and c <= 52:
                ch = "*"
            elif c == 53:
                ch = "+"
            elif c == 54:
                ch = "="
            elif c == 55:
                ch = "-"
            elif c == 56:
                ch = "="
            elif c == 57:
                ch = ":"
            elif c >= 58 and c <= 60:
                ch = "."
            elif c >= 61 and c <= 62:
                ch = ":"
            elif c >= 63 and c <= 64:
                ch = "-"
            elif c == 65:
                ch = ":"
            elif c >= 66 and c <= 67:
                ch = "."
            else:
                ch = "."
        
        # Row 32
        elif r == 32:
            if c >= 0 and c <= 15:
                ch = "."
            elif c >= 16 and c <= 18:
                ch = ":"
            elif c >= 19 and c <= 20:
                ch = "-"
            elif c >= 21 and c <= 22:
                ch = ":"
            elif c >= 23 and c <= 32:
                ch = "."
            elif c == 33:
                ch = ":"
            elif c >= 34 and c <= 35:
                ch = "-"
            elif c >= 36 and c <= 38:
                ch = "."
            elif c == 39:
                ch = ":"
            elif c == 40:
                ch = "-"
            elif c == 41:
                ch = "+"
            elif c >= 42 and c <= 43:
                ch = "#"
            elif c == 44:
                ch = "+"
            elif c == 45:
                ch = "="
            elif c == 46:
                ch = "-"
            elif c >= 47 and c <= 50:
                ch = ":"
            elif c >= 51 and c <= 53:
                ch = "-"
            elif c >= 54 and c <= 56:
                ch = ":"
            elif c >= 57 and c <= 61:
                ch = "."
            elif c == 62:
                ch = ":"
            elif c >= 63 and c <= 64:
                ch = "-"
            elif c >= 65 and c <= 67:
                ch = ":"
            elif c >= 68 and c <= 69:
                ch = "."
            else:
                ch = "."
        
        # Row 33
        elif r == 33:
            if c >= 0 and c <= 1:
                ch = "."
            elif c >= 2 and c <= 9:
                ch = ":"
            elif c >= 10 and c <= 11:
                ch = "."
            elif c >= 12 and c <= 13:
                ch = ":"
            elif c == 14:
                ch = "-"
            elif c == 15:
                ch = "="
            elif c == 16:
                ch = "-"
            elif c == 17:
                ch = ":"
            elif c >= 18 and c <= 35:
                ch = "."
            elif c >= 36 and c <= 37:
                ch = ":"
            elif c == 38:
                ch = "-"
            elif c == 39:
                ch = "+"
            elif c == 40:
                ch = "*"
            elif c >= 41 and c <= 42:
                ch = "#"
            elif c == 43:
                ch = "+"
            elif c == 44:
                ch = "="
            elif c >= 45 and c <= 54:
                ch = ":"
            elif c >= 55 and c <= 59:
                ch = "-"
            elif c >= 60 and c <= 62:
                ch = ":"
            elif c >= 63 and c <= 65:
                ch = "."
            elif c == 66:
                ch = ":"
            elif c == 67:
                ch = "="
            elif c == 68:
                ch = "-"
            elif c == 69:
                ch = ":"
            elif c >= 70 and c <= 71:
                ch = "."
            else:
                ch = "."
        
        # Row 34
        elif r == 34:
            if c >= 0 and c <= 10:
                ch = ":"
            elif c >= 11 and c <= 13:
                ch = "-"
            elif c >= 14 and c <= 15:
                ch = ":"
            elif c == 16:
                ch = "."
            elif c >= 17 and c <= 24:
                ch = ":"
            elif c >= 25 and c <= 33:
                ch = "."
            elif c == 34:
                ch = ":"
            elif c == 35:
                ch = "-"
            elif c == 36:
                ch = "="
            elif c == 37:
                ch = "*"
            elif c == 38:
                ch = "+"
            elif c == 39:
                ch = "="
            elif c >= 40 and c <= 41:
                ch = "-"
            elif c == 42:
                ch = "="
            elif c >= 43 and c <= 60:
                ch = ":"
            elif c >= 61 and c <= 64:
                ch = "-"
            elif c == 65:
                ch = "="
            elif c >= 66 and c <= 67:
                ch = "-"
            elif c >= 68 and c <= 69:
                ch = ":"
            elif c == 70:
                ch = "."
            else:
                ch = "."
        
        # Row 35
        elif r == 35:
            if c >= 0 and c <= 8:
                ch = ":"
            elif c >= 9 and c <= 10:
                ch = "-"
            elif c >= 11 and c <= 31:
                ch = ":"
            elif c == 32:
                ch = "="
            elif c == 33:
                ch = "+"
            elif c == 34:
                ch = "="
            elif c >= 35 and c <= 37:
                ch = ":"
            elif c == 38:
                ch = "-"
            elif c >= 39 and c <= 56:
                ch = ":"
            elif c >= 57 and c <= 58:
                ch = "."
            elif c >= 59 and c <= 60:
                ch = ":"
            elif c >= 61 and c <= 62:
                ch = "-"
            elif c == 63:
                ch = ":"
            elif c == 64:
                ch = "."
            elif c >= 65 and c <= 66:
                ch = ":"
            elif c == 67:
                ch = "."
            else:
                ch = "."
        
        # Row 36
        elif r == 36:
            if c >= 0 and c <= 31:
                ch = ":"
            elif c >= 32 and c <= 33:
                ch = "-"
            elif c >= 34 and c <= 38:
                ch = ":"
            elif c == 39:
                ch = "-"
            elif c >= 40 and c <= 57:
                ch = ":"
            elif c >= 58 and c <= 61:
                ch = "."
            elif c >= 62 and c <= 64:
                ch = ":"
            elif c == 65:
                ch = "."
            else:
                ch = "."
        
        # Row 37
        elif r == 37:
            if c >= 0 and c <= 32:
                ch = ":"
            elif c == 33:
                ch = "-"
            elif c >= 34 and c <= 39:
                ch = ":"
            elif c >= 40 and c <= 41:
                ch = "-"
            elif c >= 42 and c <= 57:
                ch = ":"
            elif c >= 58 and c <= 61:
                ch = "."
            elif c >= 62 and c <= 63:
                ch = ":"
            elif c == 64:
                ch = "-"
            elif c >= 65 and c <= 66:
                ch = ":"
            elif c == 67:
                ch = "."
            else:
                ch = "."
        
        # Row 38
        elif r == 38:
            if c >= 0 and c <= 8:
                ch = ":"
            elif c >= 9 and c <= 12:
                ch = "-"
            elif c >= 13 and c <= 15:
                ch = ":"
            elif c >= 16 and c <= 24:
                ch = "-"
            elif c >= 25 and c <= 26:
                ch = ":"
            elif c >= 27 and c <= 31:
                ch = "-"
            elif c == 32:
                ch = ":"
            elif c >= 33 and c <= 35:
                ch = "-"
            elif c == 36:
                ch = ":"
            elif c == 37:
                ch = "-"
            elif c == 38:
                ch = ":"
            elif c == 39:
                ch = "="
            elif c == 40:
                ch = "-"
            elif c == 41:
                ch = ":"
            elif c == 42:
                ch = "-"
            elif c == 43:
                ch = ":"
            elif c >= 44 and c <= 45:
                ch = "-"
            elif c >= 46 and c <= 50:
                ch = ":"
            elif c >= 51 and c <= 52:
                ch = "-"
            elif c >= 53 and c <= 57:
                ch = ":"
            elif c == 58:
                ch = "-"
            elif c >= 59 and c <= 62:
                ch = ":"
            elif c >= 63 and c <= 64:
                ch = "-"
            elif c >= 65 and c <= 67:
                ch = ":"
            elif c == 68:
                ch = "."
            else:
                ch = "."
        
        line = line + ch
    print(line)
