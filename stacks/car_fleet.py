from typing import List
import math


class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        car_fleet = []
        steps = sorted(
            [
                (
                    position[i],
                    (target - position[i]) / speed[i],
                )
                for i in range(len(position))
            ],
            key=lambda x: x[0],
        )

        for index in range(len(steps)):
            while car_fleet and car_fleet[-1][1] <= steps[index][1]:
                car_fleet.pop()
            car_fleet.append(steps[index])

        return len(car_fleet)


if __name__ == "__main__":
    test = Solution()
    print(
        test.carFleet(target=10, position=[8, 3, 7, 4, 6, 5], speed=[4, 4, 4, 4, 4, 4])
    )
