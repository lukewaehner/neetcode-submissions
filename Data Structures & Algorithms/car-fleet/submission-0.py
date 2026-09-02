class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        c = sorted(zip(position, speed), reverse=True)
        for i in range(len(speed)):
            ttt = (target - c[i][0]) / c[i][1]
            if not stack:
                stack.append(ttt)
            elif ttt > stack[-1]:
                stack.append(ttt)
        return len(stack)
