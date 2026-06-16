from sympy import symbols
from sympy.logic.boolalg import And, Or, Not, Implies, Equivalent
from sympy.logic.inference import satisfiable


def define_knowledge_base():
    """Define predicates and knowledge rules"""

    # Define predicates
    Rain = symbols('Rain')
    Traffic = symbols('Traffic')
    Accident = symbols('Accident')
    Late = symbols('Late')

    # Define knowledge rules using logical expressions
    rule1 = Implies(Rain, Traffic)
    rule2 = Implies(Traffic, Late)
    rule3 = Implies(Accident, Traffic)
    rule4 = Equivalent(Late, Or(Traffic, Accident))

    knowledge_base = [rule1, rule2, rule3, rule4]

    return knowledge_base, Rain, Traffic, Accident, Late


def evaluate_scenario(knowledge_base, assumptions):
    """Evaluate the scenario based on given assumptions"""

    scenario = And(*knowledge_base, *assumptions)

    result = satisfiable(scenario)

    return result


if __name__ == "__main__":

    # Define knowledge base
    knowledge_base, Rain, Traffic, Accident, Late = define_knowledge_base()

    # Scenario 1 raining
    print("Scenario 1: It is raining")
    assumptions = [Rain]
    result = evaluate_scenario(knowledge_base, assumptions)
    print("Outcome:", result, "\n")

    # Scenario 2 accident
    print("Scenario 2: There is an accident")
    assumptions = [Accident]
    result = evaluate_scenario(knowledge_base, assumptions)
    print("Outcome:", result, "\n")

    # Scenario 3 both
    print("Scenario 3: It is raining and there is an accident")
    assumptions = [Rain, Accident]
    result = evaluate_scenario(knowledge_base, assumptions)
    print("Outcome:", result)