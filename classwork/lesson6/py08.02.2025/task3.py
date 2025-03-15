from math import sqrt

# points_list = [[1, 1], [4, 5], [7, 1], [-1, 3], [4, 4]]

# def distance(points):
#     max_distance = 0
#     point1_max = None  
#     point2_max = None  
#     for i in range(len(points)): 
#         for j in range(i + 1, len(points)):
#             point1 = points[i]
#             point2 = points[j]

            
#             distance_value = sqrt((point2[0] - point1[0])**2 + (point2[1] - point1[1])**2)

            
#             if distance_value > max_distance:
#                 max_distance = distance_value
#                 point1_max = point1
#                 point2_max = point2

#     return point1_max, point2_max, max_distance

# point1, point2, max_dist = distance(points_list)

# if point1 and point2:
#     print(f"Точка 1: {point1}")
#     print(f"Точка 2: {point2}")
#     print(f"Максимальное расстояние: {max_dist}")

def is_point_inside_circle(center_x, center_y, radius, point_x, point_y):
    
    distance_from_center_squared = (point_x - center_x)**2 + (point_y - center_y)**2
    radius_squared = radius**2

    return distance_from_center_squared <= radius_squared

center_x_circle = 1 
center_y_circle = 2  
radius_circle = 5     
x_point = 3           
y_point = 4           


print(is_point_inside_circle(center_x_circle, center_y_circle, radius_circle, x_point, y_point))
