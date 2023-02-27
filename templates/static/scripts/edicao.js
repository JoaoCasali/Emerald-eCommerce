$(document).ready(function () {
    $('input[required]').next('label').append('<span> *</span>');

    // verificação de caracteres válidos
    $('.decimal').keypress(function (event) {
        if (event.which !== 8 && event.which !== 0 && event.which < 48 || event.which > 57) {
            event.preventDefault();
        }
    });

    $('.data').keypress(function (event) {
        if ((event.which < 48 || event.which > 57) && event.which !== 47 && event.which !== 45 && event.which !== 46) {
            event.preventDefault();
        }
    });

    // formatadores
    $('.decimal').blur(function () {
        var valor = parseFloat($(this).val()).toLocaleString('pt-BR', { minimumFractionDigits: 2 });
        $(this).val(valor);
    });

    $('.data').blur(function () {
        var valor = $(this).val();
        var data = moment(valor, ['DD/MM/YYYY', 'D/M/YYYY', 'DDMMYYYY', 'DD.MM.YYYY', 'DD-MM-YYYY'], true);
        if (data.isValid()) {
            $(this).val(data.format('DD/MM/YYYY'));
        } else {
            $(this).val('');
        }
    });
});

function DefinirCampoComoObrigatorio(campo) {
    campo.next('label').append('<span> *</span>')
}

function DefinirCampoComoOpcional(campo) {
    campo.removeAttr('required');
    campo.next('label').find('span').remove();
}