# import os,sys,inspect
# current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
# parent_dir = os.path.dirname(current_dir)
# sys.path.insert(0, parent_dir)
# sys.path.insert(0, os.path.dirname(parent_dir))
#
# import bandit
#
# def simulate():
#     """
#     Test-runner for comparing the Epsilon-decaying bandit vs a naive
#     epsilon-greedy bandit.
#
#     dv17pft
#     et16btt
#     """
#
#     results = []
#     for _ in range(0, 20):
#         sys.stdout.write("\033[1;36m")
#         bandit_reward = bandit.simulator.simulate(bandit.bandit)
#         sys.stdout.write("\033[0;0m")
#         ref_bandit_reward = bandit.simulator.simulate(bandit.ref_bandit)
#         ref_plus_bonus = ref_bandit_reward * 1000
#         result = 0
#         if (bandit_reward > ref_plus_bonus):
#             result = 1
#             sys.stdout.write("\033[1;32m")
#             print("Win!")
#             sys.stdout.write("\033[0;0m")
#         else:
#             sys.stdout.write("\033[1;31m")
#             print("Loss!")
#             sys.stdout.write("\033[0;0m")
#
#         results.append(result)
#     return results
#
# def test_performance():
#     assert sum(simulate()) > 17
