# Calculate the area of a triangle, square, and a rectangle.

def calc_area(polygon, base, height):
  polygon = polygon.lower()

  if polygon == 'triangle':
    area = base * height / 2
  elif polygon in ['square','rectangle']:
    area = base * height
  else:
    print('No valid polygon')
    return
  
  print(f'The area of the {polygon} is {area}')


# Test cases
calc_area('rectangle', 6, 4)
calc_area('square', 6, 6)
calc_area('triangle', 7, 6)
calc_area('pentagon', 5, 8)  # Testing with an invalid polygon