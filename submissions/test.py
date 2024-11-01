from strats import *

class Strategy(Hard):
    engg_question_limit = 3

    
    
        

    def solve(game):
        A, B, C, D = Alice, Bob, Charlie, Dan
        q1 , q2, q3, q4 = Foo, Foo, Foo, Baz
        b1, b2, b3, b4 = False, False, False, True

        e1, e2, e3, e4 = True, True, True, True
        # p1, p2, p3, p4 = True, True, True, True
        b1, b2, b3, b4 = True, True, True, True
      
        q1 = game.get_response( A.ask( A.ask( Baz != A.ask(true) && Baz != A.ask(false) ) == Baz) ) # Using Baz > Baz, else > false
        q2 = game.get_response( B.ask( B.ask( Baz != B.ask(true) && Baz != B.ask(false) ) == Baz) ) # Using Baz > Baz, else > false
        
        b1, b2 = q1 == q4, q2 == q4
        
        if (q1 == q2):
            if(b1):
                #s ometing
                # q3 = game.get_response(    A.ask(    A.ask( C.
            else:
                e3, e4 = False, False
                q3 = game.get_response( C.ask(  not( A.studies(Phil) or B.studies(Phil) ) ) )
                if (q3 == q1):
                    q3 = game.get_response( C.ask( C.studies(Math) or C.studies ) )
                    game.guess[D] = Phil
                    
                    
                    
                    q4 = game.get_response( C.ask( A.studies(Engg) ) )
                    if (q3 == q1):
                        game.guess[C] = Math
                        if (q4 == q1):
                            game.guess[A] = Engg
                            game.guess[B] = Phis
                        else:
                            game.guess[A] = Phis
                            game.guess[B] = Engg
                    else:
                        game.guess[C] = Phys
                        if (q4 == q1):
                            game.guess[A] = Engg
                            game.guess[B] = Math
                        else:
                            game.guess[A] = Math
                            game.guess[B] = Engg
                    return 0;
        else:
            if(b1 or b2):
                
                
                
        
        
        q3 = game.get_response( C.ask( C.ask( Baz != C.ask(true) && Baz != C.ask(false) ) == Baz) ) # Using Baz > Baz, else > false
          
        b1, b2, b3, b4 = q1 == q4, q2 == q4, q3 == q4, True
  
        if not (b1 or b2 or b3):
            game.guess[D] = Phil
            if q1 == q2:
                game.get_response( C.ask( C.ask(  ) == Foo) )



        
        c_is_math = game.ask(C, C.studies(Math)) 
        self.guess[A] = Engg
        self.guess[B] = Phys if c_is_math else Math
        self.guess[C] = Math if c_is_math else Phys
