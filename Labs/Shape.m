classdef Shape
    
    properties
        name
        number_of_edges
    end

    methods
        function obj = Shape(name, number_of_edges)
            obj.name = name;
            obj.number_of_edges = number_of_edges;
        end
    end
    
end