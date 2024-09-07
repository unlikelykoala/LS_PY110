Input: number of available blocks (integer)
Output: number of blocks left over after building the tallest possible valid structure (integer)

Explicit rules:
    - use building blocks to create a structure
    - the blocks are cubes (6 sides)
    - the structure is built in layers
    - top layer is a single block
    - a block in an upper layers must be supported by 4 blocks in a lower layer
    - a block in a lower layer can support more than one block in an upper layer.
    - no gaps between blocks

Implicit rules:
    - lower layers will always have more blocks than upper layers
    - num of blocks per layer = layer_number**2

Questions:
    - how many upper blocks can 1 lower block support? 4?
    - test case / question: will an upper layer of 2 blocks need to be supported by at least 6 blocks?
    - how to compose layers?

Visualize:
    - Top layer: 1 block (1x1)
    - 2nd: 4 blocks (2x2)
    - 3rd: 9 blocks (3x3)

Step 2 notes after seeing test cases:
    - 0 rows returns 0 blocks
    - a row cannot have more blocks than it needs

Data Structures:
    - integers for the input, output, and calculations
    - list: 0th index is top row (1 or 0), and moving up an index is like moving up a layer

Algorithm:
    1. Get input: number of layers (integer)
    2. Loop until # of blocks for new row is less than remainder
        A. Calculate blocks for row
        1. use % to get remainder
        B. if the next square number < remainder, return remainder
        C. Else: create next row and proceed with the loop