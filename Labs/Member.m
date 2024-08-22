classdef Member
    properties
        name = "Joel Miller"
        ID = 12345678
    end

    methods
        function obj = Member(name, ID)
            if nargin == 2
                obj.name = name;
                obj.ID = ID;
            end
        end
    end
end