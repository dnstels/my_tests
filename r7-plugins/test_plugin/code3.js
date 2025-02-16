(function(window, undefined){
    window.Asc.plugin.init = function() {
        window.myVar=parent.AscDesktopEditor.LocalFileGetSourcePath();
        function myFunc(docCanSave) {
            Asc.scope.text=docCanSave;
            Asc.scope.st="-";
        };
        if(typeof Asc.scope.st === "undefined"){
            this.callCommand(function() {
                var sheets = Api.GetSheets();
                window.myVar_int=sheets;
                if(typeof Asc.scope.text === "undefined"){
                    var res=[];
                    sheets.forEach(s=>res.push(s.GetName()))
                }
                // Asc.scope.text=["-",sheets[0].GetName()];
                Asc.scope.st="-";
                return res;
            },false,true,myFunc);
        };
        Asc.scope.st="-";
    };
    window.Asc.plugin.button = function(id)
    {
        console.log(id);
        if(id!=0)
            this.executeCommand("close", null);
        else{
        window.myVar_int=Asc.scope.text;
        doStart();
        }
    };
})(window, undefined);