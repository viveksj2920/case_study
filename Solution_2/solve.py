class GraduationCeremony:
    def __init__(self, x):
        self.x = x
        
    def solve(self):
        num_academic_days, missed_classes = self.x, 4
        if num_academic_days <1:
            raise ValueError("The input must be a positive integer.")
        dp = [[0] * (missed_classes + 1) for _ in range(num_academic_days + 1)]

        for i in range(missed_classes):
            dp[0][i] = 1

        for i in range(1, num_academic_days + 1):
            for j in range(missed_classes - 1, -1, -1):
                dp[i][j] = dp[i - 1][0] + dp[i - 1][j + 1]

        total_ways_to_attend = dp[num_academic_days][0]
        total_ways_to_not_attend_last_day = dp[num_academic_days - 1][1]
        return f"{total_ways_to_not_attend_last_day}/{total_ways_to_attend}"
    

    def execute(self):
        print("--" * 10)
        print('Total number of college days:', self.x, "Total number of missed classes:", 4, '\n')
        print()
        print("Result", self.solve())
        print('**' * 10)
        print()

