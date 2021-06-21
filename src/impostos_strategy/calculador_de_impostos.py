class Calculador_de_impostos(object):

  def realiza_calculo(self, orcamento, imposto):

    if 'ICMS' == imposto:
      icms_calculado = orcamento.valor * 0.1
      print(icms_calculado)

    elif 'ISS' == imposto:
      iss_calculado = orcamento.valor * 0.06
      print(iss_calculado)

if __name__ == '__main__':

    from orcamento import Orcamento

    orcamento = Orcamento(500.0)
    calculador_de_impostos = Calculador_de_impostos()
    calculador_de_impostos.realiza_calculo(orcamento, 'ICMS') # imprimirá 50
    calculador_de_impostos.realiza_calculo(orcamento, 'ISS') # imprimirá 30
