(function(window, undefined){
    var text = "Hello world!";
    var abc = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя";
    var random = abc[Math.floor(Math.random() * abc.length)];
        while (text.length < 20) {
        text+=random;
        random = abc[Math.floor(Math.random() * abc.length)];
        }
    text=parent.AscDesktopEditor.LocalFileGetSourcePath();
    window.Asc.plugin.init = function() {
        Asc.scope.text = text;
        this.callCommand(function() {
            var oWorksheet = Api.GetActiveSheet();
            console.log(Asc.scope.text);
            var oSheet = Api.AddSheet("Sheet2");
            var oWorksheet = Api.GetActiveSheet();
            var link='=ГИПЕРССЫЛКА("'+Asc.scope.text+'","ССЫЛКА")';
            oWorksheet.GetRange("A1").SetValue(link);
        }, true);
    };
    window.Asc.plugin.button = function(id)
    {
    };
})(window, undefined);