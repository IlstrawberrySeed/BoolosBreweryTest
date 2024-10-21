"""
Sample strategy, to demonstrate how to implement one.
"""

from strats import *

class Strategy(Easy):
    """
    The strategy must be implemented in a class called "Strategy", which derives from the appropriate difficulty level.
    Difficulty levels: Easy, Default, Hard.
    """

    # The Solver class must have a static parameter `engg_question_limit`, which specifies an upper bound for how many
    # questions you may end up asking the engineer.
    # You can go under this number, but you can't go over, or the game will crash.
    # Note: this quantity determines submission runtime (the relationship is exponential), so try to use a tight upper
    # bound if possible!
    # In our case, since we're solving the Easy variant of the puzzle, engg_question_limit can be zero
    # (there are no engineers present).
    engg_question_limit = 0

    def solve(game):
        """
        This is the entrypoint for solving the puzzle.
        When invoked, a game instance is already running.
        Invoke "self.ask" to pass a Question instance to the game.
        The return value will be a Response instance.

        When you believe you have solved the puzzle (in `question_limit` or fewer), call "self.guess".
        This function takes an assignment of Alice, Bob[, Charlie[, Dan]] to Field instances.
        """

        # Step 1: find the person who says "foo" as "yes"
        alice_yes = game.get_response(Alice.ask(True))
        bob_yes = game.get_response(Bob.ask(True))

        if alice_yes == Foo:
            assert(bob_yes == Bar)
            foo_sayer = Alice
            bar_sayer = Bob
        else:
            assert(bob_yes == Foo)
            foo_sayer = Bob
            bar_sayer = Alice

        # Step 2: ask the foo-sayer if they study math
        foo_math = game.get_response(foo_sayer.ask(foo_sayer.studies(Math)))
        if foo_math is Foo:
            # foo-sayer is a mathematician!
            game.guess[foo_sayer] = Math
        else:
            # foo-sayer must be a physicist!
            game.guess[foo_sayer] = Phys

        # Step 3: for good measure, ask bar-sayer if they study math
        bar_math = game.get_response(foo_sayer.ask(bar_sayer.studies(Math)))
        if bar_math is Foo:
            # bar-sayer is a mathematician!
            game.guess[bar_sayer] = Math
        else:
            # bar-sayer must be a physicist!
            game.guess[bar_sayer] = Phys

        
        # When the function exits, the contents of `game.guess` will be checked.
        # Make sure game.guess[Alice] and game.guess[Bob] are both Field instances
        # (and that game.guess[Charlie] and game.guess[Dan] are None)


