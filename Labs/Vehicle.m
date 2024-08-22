classdef Vehicle

    properties
        name
        max_speed
    end

    methods
        function obj = Vehicle(name, max_speed)
            obj.name = name;
            obj.max_speed = max_speed;
        end
    end
end