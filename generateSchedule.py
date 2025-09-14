class Solution:
    def scheduleMatches(self, n: int) -> List[List[int]]:
        num_of_team=n
        if num_of_team<4:
            return []
        clubs=list(range(num_of_team))
        rounds=[]
        if num_of_team%2==1:
            clubs.append(-1)  
            num_of_team+= 1
        half_size = num_of_team // 2
        for r in range(num_of_team-1):
            day_matches = []
            for i in range(half_size):
                t1, t2 = clubs[i], clubs[-1 - i]
                if t1 != -1 and t2 != -1:
                    day_matches.append([t1, t2])
            rounds.append(day_matches)
            clubs = [clubs[0]] + [clubs[-1]] + clubs[1:-1]
        fixtures = []
        for block in rounds:
            fixtures.extend(block)
        for block in rounds:
            for h, a in block:
                fixtures.append([a, h])
        arranged = []
        used = [False] * len(fixtures)
        last_day = set()
        for _ in range(len(fixtures)):
            placed = False
            for i, game in enumerate(fixtures):
                if not used[i]:
                    home, away=game
                    if home not in last_day and away not in last_day:
                        arranged.append(game)
                        used[i] = True
                        last_day ={home, away}
                        placed=True
                        break
            if not placed:
                return []
        return arranged
