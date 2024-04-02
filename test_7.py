from solution_7 import TrafficLight

light_name = TrafficLight()
print(light_name.current_signal)
for _ in range(10):
    light_name.next_signal()
    print(light_name.current_signal)
print(light_name)
b = [light_name]
print(b)
