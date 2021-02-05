CREATE TABLE IF NOT EXISTS stats(
    time timestamp PRIMARY KEY DEFAULT now(),
    intemp smallint  NOT NULL,   -- temperature inside at current time
    outtemp smallint NOT NULL,   -- temperature outside at current time
    settemp smallint NOT NULL,   -- assigned by user
    hvac_cost money NOT NULL,    -- cost of temperature regulation inside, since last
    power_con smallint NOT NULL, -- kWh consumed since last time
    power_cost money NOT NULL,   -- cost of above
    water_con smallint NOT NULL, -- gallons consumed since last time
    water_cost money NOT NULL    -- cost of above
);


CREATE TABLE IF NOT EXISTS light(
    lights_id int UNIQUE default(1) PRIMARY KEY, -- CANNOT CHANGE, DO NOT ATTEMPT
    masterbedroom boolean NOT NULL DEFAULT false,
    masterbathroom boolean NOT NULL DEFAULT false,
    livingroom boolean NOT NULL DEFAULT false,
    kitchen boolean NOT NULL DEFAULT false,
    bedroom boolean NOT NULL DEFAULT false,
    closet boolean NOT NULL DEFAULT false,
    bathroom_a boolean NOT NULL DEFAULT false,
    bathroom_b boolean NOT NULL DEFAULT false,
    garage boolean NOT NULL DEFAULT false,
    office boolean NOT NULL DEFAULT false,
    playroom boolean NOT NULL DEFAULT false,
    front boolean NOT NULL DEFAULT false,
    patio boolean NOT NULL DEFAULT false,
    CONSTRAINT light_singleton CHECK (lights_id = 1)
);

CREATE TABLE IF NOT EXISTS door(
    doors_id int UNIQUE default(1) PRIMARY KEY, -- CANNOT CHANGE, DO NOT ATTEMPT
    masterbedroom boolean NOT NULL DEFAULT false,
    masterbathroom boolean NOT NULL DEFAULT false,
    livingroom boolean NOT NULL DEFAULT false,
    kitchen boolean NOT NULL DEFAULT false,
    bedroom boolean NOT NULL DEFAULT false,
    closet boolean NOT NULL DEFAULT false,
    bathroom_a boolean NOT NULL DEFAULT false,
    bathroom_b boolean NOT NULL DEFAULT false,
    garage boolean NOT NULL DEFAULT false,
    office boolean NOT NULL DEFAULT false,
    playroom boolean NOT NULL DEFAULT false,
    front boolean NOT NULL DEFAULT false,
    patio boolean NOT NULL DEFAULT false,
    CONSTRAINT doors_singleton CHECK (doors_id = 1)
);


CREATE TABLE IF NOT EXISTS window(
    windows_id int UNIQUE default(1) PRIMARY KEY, -- CANNOT CHANGE, DO NOT ATTEMPT
    masterbedroom boolean NOT NULL DEFAULT false,
    masterbathroom boolean NOT NULL DEFAULT false,
    livingroom boolean NOT NULL DEFAULT false,
    kitchen boolean NOT NULL DEFAULT false,
    bedroom boolean NOT NULL DEFAULT false,
    closet boolean NOT NULL DEFAULT false,
    bathroom_a boolean NOT NULL DEFAULT false,
    bathroom_b boolean NOT NULL DEFAULT false,
    garage boolean NOT NULL DEFAULT false,
    office boolean NOT NULL DEFAULT false,
    playroom boolean NOT NULL DEFAULT false,
    front boolean NOT NULL DEFAULT false,
    patio boolean NOT NULL DEFAULT false,
    CONSTRAINT windows_singleton CHECK (windows_id = 1)
);
