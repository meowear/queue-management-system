def calculate_wait_time(position: int, exits: int, interaction_time: int) -> int:
    """
    Calculates estimated wait time based on parallel service formula.
    Wait Time = (Position / Number of Exits) * Interaction Time
    """
    if exits <= 0:
        raise ValueError("Number of exits must be greater than zero.")
    
    # We use floor division for position/exits or should we use float and then round?
    # The requirement says (Position / Service Points) * Interaction Time.
    # Usually in queuing, it's (position // exits) * interaction_time.
    # Example: Pos 1-2 with 2 exits -> 0 mins wait (they are being served).
    # Pos 3-4 with 2 exits -> interaction_time wait.
    # Let's use (position // exits) * interaction_time.
    
    # Actually, if I'm at position 10 and there are 2 exits.
    # 10 // 2 = 5. 5 * 5 = 25 mins.
    # If I'm at position 1 and there are 2 exits.
    # 1 // 2 = 0. 0 * 5 = 0 mins. (I'm being served).
    
    return (position // exits) * interaction_time
