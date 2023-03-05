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

    $('.cpf_cnpj').keypress(function (event) {
        var tecla = event.which;
        if (tecla != 8 && tecla != 0 && tecla != 45 && tecla != 47 && (tecla < 48 || tecla > 57)) {
            event.preventDefault();
        }
    });

    // formatadores
    $('.decimal').blur(function () {
        if ($(this).val() == '') {
            return
        }
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

    $(".cpf_cnpj").blur(function () {
        var value = $(this).val();
        value = value.replace(/[^0-9]/g, "");
        if (value == '') {
            return
        }
        var length = value.length;
        var formatted_value = "";

        if (length == 11) {
            formatted_value = value.replace(/(\d{3})(\d{3})(\d{3})/, "$1.$2.$3-");
        }
        else if (length == 14) {
            formatted_value = value.replace(/(\d{2})(\d{3})(\d{3})(\d{4})(\d{2})/, "$1.$2.$3/$4-$5");
        }
        else {
            $(this).val("");
        }

        $.ajax({
            url: makeUrl("Auth/VerificarCNPJ?cnpj=") + value,
            type: 'GET',
            async: false,
            dataType: 'json',
            success: function (response) {
                if (response.Resposta == false) {
                    alert('CNPJ inválido');
                    $('#cpf_cnpj').val('');
                } else {
                    $(this).val(formatted_value);
                }
            },
            error: function (xhr, status, error) {
                alert(error);
            }
        });

    });
});

function DefinirCampoComoObrigatorio(campo) {
    campo.next('label').append('<span> *</span>')
}

function DefinirCampoComoOpcional(campo) {
    campo.removeAttr('required');
    campo.next('label').find('span').remove();
}