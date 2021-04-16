# Map
cell_size = 40                      # Größe der Zellen
cell_number = 20

# Display
xSize = cell_size * cell_number     # Display-Größe X
ySize = cell_size * cell_number     # Y
FPS = 60                            # Frames per Second
SPEED = 150                         # Spielgeschwindigkeit
FONT_SIZE = 65                      # Fontgröße
PREVIEW_SIZE = 65                   # Bildgröße bei Score-Anzeige

# Gameplay
MAX_ELEMENTS_ON_MAP = 3             # Anzahl der Gesamt-Elemente auf der Map (kein Einfluss auf Spawning_mouse_on_cheese)
CUTTING = -6                        # Anzahl der abziehbare Blöcke der Schlange bei Säge
TIME_TO_SLOW = 20                   # Ticks für Timeslow für Zeituhr
SPAWNING_MOUSE_ON_CHEESE = 3        # Anzahl Mäuse nach Käse
STRECH_COUNT = 4                    # Anzahl Blöcke für Schlange nach Cake
TIME_TO_REVERSE = 20                # Ticks für Reverrse für Poison

# Probability für food_items außer Maus (siehe unten)
PROBABILITY_FOR_CAKE = 1
PROBABILITY_FOR_SANDGLASS = 1
PROBABILITY_FOR_CHEESE = 1
PROBABILITY_FOR_SAW = 1
PROBABILITY_FOR_PEEL = 1
PROBABILITY_FOR_POISON = 1

# Probability für Mouse in % (z.B 0.6 oder 0.3)
PROBABILITY_FOR_MOUSE = 0.7

# Score system
SCOREPOINTS_MAUSE = 5
SCOREPOINTS_SAW = 1
SCOREPOINTS_CHEESE = 2 
SCOREPOINTS_SANDGLASS = 2
SCOREPOINTS_CAKE = 1

