import time

class PomodoroTimer:
    def __init__(self, work_timer=30*60, rest_timer=5*60, long_rest_timer=15*60, pomo_rep=3):
        self.work_timer = work_timer
        self.rest_timer = rest_timer
        self.long_rest_timer = long_rest_timer
        self.pomo_rep = pomo_rep

    def change_default(self, prompt: str) -> bool:
        while True:
            response = input(prompt).strip().upper()
            if response in ['Y', 'N']:
                return response == 'Y'
            print('Invalid input! Please enter Y or N.')

    def cronometer(self, timer: int) -> None:
        for remaining in range(timer, 0, -1):
            minutes, seconds = divmod(remaining, 60)
            print(f'{minutes:02}:{seconds:02}', end='\r')
            time.sleep(1)
        print()

    def run_pomodoro(self, pomodoro_times: int) -> None:
        for _ in range(pomodoro_times):
            for _ in range(self.pomo_rep):
                print('\nWORK TIME!💻')
                self.cronometer(self.work_timer)
                if _ < self.pomo_rep - 1:
                    print('\nBREAK TIME!🍩')
                    self.cronometer(self.rest_timer)
            print('\nLONG BREAK!🌤')
            self.cronometer(self.long_rest_timer)
        print('\nCongratulations! You finished! Go Touch Some Grass! 🌲')

    def configure(self) -> None:
        print('\nThe default timers are:')
        print('💻 Work time: 30 min')
        print('🍩 Break time: 5 min')
        print('🌴 Long Break: 15 min')

        if self.change_default('\nDo you want to change the timers? [Y/N]: '):
            self.work_timer = int(input('💻 Work Time (in minutes): ')) * 60
            self.rest_timer = int(input('🍩 Break Time (in minutes): ')) * 60
            self.long_rest_timer = int(input('🌴 Long Break (in minutes): ')) * 60

        if self.change_default('\nDo you want to change the number of repetitions before a long break? [Y/N]: '):
            self.pomo_rep = int(input('\nEnter the number of repetitions: '))

def main():
    try:
        pomodoro_times = int(input('How many times to run pomodoro? 🍅: '))
        pomodoro_timer = PomodoroTimer()
        pomodoro_timer.configure()
        pomodoro_timer.run_pomodoro(pomodoro_times)
    except ValueError as e:
        print(f'Invalid input: {e}')
    except Exception as e:
        print(f'An error occurred: {e}')

if __name__ == '__main__':
    main()
