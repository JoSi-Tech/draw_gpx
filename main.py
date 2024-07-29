import draw
# to do 
# načital sio zoznam GPX suborov

gpx_files = ['Morning_Run.gpx']  # List of GPX files
img_width, img_height = 800, 600  # Resolution of the image
bg_color = (255, 255, 255)  # Background color (white)
path_color = (0, 0, 0)  # Path color (black)
output_file = 'blind_map.png'  # Output file name

draw.create_blind_map(gpx_files, img_width, img_height, bg_color, path_color, output_file)