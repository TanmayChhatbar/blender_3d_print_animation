## Setup and Execution Instructions

- Use PrusaSlicer to slice an object (The instructions have been tested for version 2.5.0).
- To generate 'pathout.csv', use the following command: 
`python path_follower.py {gcode_file.gcode}`
- Open the file `Ender 3_follow_path.blend`
- Navigate to the scripting tab and execute the `mesh-working` script.
- Position the STL object in the 3D printer.
- Assign the '3dp' material to the object.
- Set up boolean difference modifier with Object 'print_bool'
- Run the setup to ensure everything functions as expected.

## Assistance and Contribution
- Reach out to me if you have any questions
- For those interested in advancing this project, you're welcome! Please do attribute the original work in your improvements. I look forward to seeing what enhancements you bring to this project!

## Sample
https://user-images.githubusercontent.com/14368465/219824015-7bb71b1a-3df8-4cc7-83f9-0bd82c115646.mp4

## Credits
- Ender 3 model from https://github.com/Creality3DPrinting/Ender-3/tree/master/Ender-3%20Mechanical/STP
