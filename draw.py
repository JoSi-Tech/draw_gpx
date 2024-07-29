import gpxpy
import gpxpy.gpx
from PIL import Image, ImageDraw

def parse_gpx(file_path):
    with open(file_path, 'r') as gpx_file:
        gpx = gpxpy.parse(gpx_file)
    coordinates = []
    for track in gpx.tracks:
        for segment in track.segments:
            for point in segment.points:
                coordinates.append((point.latitude, point.longitude))
    return coordinates

def normalize_coordinates(coordinates, img_width, img_height):
    lats = [coord[0] for coord in coordinates]
    lons = [coord[1] for coord in coordinates]
    min_lat, max_lat = min(lats), max(lats)
    min_lon, max_lon = min(lons), max(lons)

    def normalize(lat, lon):
        x = (lon - min_lon) / (max_lon - min_lon) * (img_width - 1)
        y = (1 - (lat - min_lat) / (max_lat - min_lat)) * (img_height - 1)
        return (int(x), int(y))

    return [normalize(lat, lon) for lat, lon in coordinates]

def create_blind_map(gpx_files, img_width, img_height, bg_color, path_color, output_file):
    image = Image.new('RGB', (img_width, img_height), color=bg_color)
    draw = ImageDraw.Draw(image)
    
    for gpx_file in gpx_files:
        coordinates = parse_gpx(gpx_file)
        if coordinates:
            normalized_coords = normalize_coordinates(coordinates, img_width, img_height)
            draw.line(normalized_coords, fill=path_color, width=2)
    
    image.save(output_file)

gpx_files = ['Morning_Run.gpx']  # List of GPX files
img_width, img_height = 800, 600  # Resolution of the image
bg_color = (255, 255, 255)  # Background color (white)
path_color = (0, 0, 0)  # Path color (black)
output_file = 'blind_map.png'  # Output file name

create_blind_map(gpx_files, img_width, img_height, bg_color, path_color, output_file)