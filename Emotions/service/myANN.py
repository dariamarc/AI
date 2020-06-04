import random
import numpy as np
from sklearn.metrics import log_loss


def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def sigmoid_dx(x):
    return x * (1 - x)

class NeuralNetwork:
    def __init__(self, noHiddenLayers, dimHiddenLayers, noIter):
        self.noHiddenLayers = noHiddenLayers
        self.dimHiddenLayers = dimHiddenLayers
        self.noIter = noIter
        self.coefs = []

    def fit(self, inputs, outputs, alpha):
        # coefs = [[[w0, w3, w6, w9], [w1, w4, w7, w10], ...], [coeficientii dintre hiddenLayer1 si
        # hiddenLayer2 sub forma [w care intra in primul neuron], [w care intra in al doilea neuron]],
        # ..., [coeficientii dintre hiddenLayern si output]]

        # adaugare coeficienti dintre input si hiddenLayer1
        w_inputs = []
        for _ in range(self.dimHiddenLayers):
            w_inputs.append([random.random() for _ in range(len(inputs[0]))])

        self.coefs.append(w_inputs)
        # adaugare coeficienti dintre hiddenLayers
        for _ in range(self.noHiddenLayers - 1):
            w = []
            for _ in range(self.dimHiddenLayers):
                w.append([random.random() for _ in range(self.dimHiddenLayers)])
            self.coefs.append(w)


        # adaugare coeficienti dintre ultimul hiddenLayer si output
        w_outputs = []
        for _ in range(len(set(outputs))):
            w_outputs.append([random.random() for _ in range(self.dimHiddenLayers)])

        self.coefs.append(w_outputs)

        for i in range(self.noIter):
            print('Iteration ' + str(i) + '.............')
            computed = []
            probs = []
            for input_idx in range(len(inputs)):
                # forward feed
                neurons_inputs = []
                neurons_outputs = []
                x = inputs[input_idx]
                # print('Input layer :')
                # print(x)
                for no_layer in range(len(self.coefs)):
                    # pentru fiecare layer iau input-ul pe care il primeste (x) si calculez
                    # output-ul fiecarui neuron, dupa care il adaug in lista (x) pentru a fi
                    # input pentru urmatorul strat de neuroni
                    # print('Layer no. ' + str(no_layer + 1))
                    '''
                    Clarificare:
                        - neurons_outputs = output-urile date de fiecare strat de neuroni
                         = [[outNhidd1, outNhidd2, outNhidd3, outNhidd4], [outNout1, outNout2]]
                         pentru a putea folosi asta la back-propagation se adauga si input-ul la inceputul
                         listei
                         - output-error: eroarea pe stratul de output
                         = [errOut1, errOut2, ...]
                         - errors: erorile pentru straturile ascunse si stratul de inceput
                         = [[errIn1, errIn2, ...], [errHidd1, errHidd2, ...], ...]
                    '''

                    neurons_inputs.append(x)
                    out = []
                    for no_w in range(len(self.coefs[no_layer])):
                        value = 0.0
                        for w_idx in range(len(self.coefs[no_layer][no_w])):
                            value += x[w_idx] * self.coefs[no_layer][no_w][w_idx]
                        out.append(sigmoid(value))
                    x = out
                    neurons_outputs.append(x)
                    # print(x)

                # acum x-ul este ce scoate layer-ul de output si se face un softmax
                output_sum = sum(x)
                x = [nr / output_sum for nr in x]
                neurons_outputs.remove(neurons_outputs[-1])
                neurons_outputs.append(x)
                # all_outputs.append(neurons_outputs)
                    # print(x)


                neurons_outputs.insert(0, inputs[input_idx])
                #print(neurons_outputs)

                # back propagation
                # eroare corespunzatoare stratului de iesire
                output_error = []
                for out_idx in range(len(neurons_outputs[-1])):
                    output_error.append((outputs[input_idx] - neurons_outputs[-1][out_idx]) * sigmoid_dx(neurons_outputs[-1][out_idx]))
                # print(output_error)

                errors = []
                # erorile pentru straturile ascunse
                for back_idx in range(self.noHiddenLayers, 0, -1):
                    # print(back_idx)
                    err = []    # eroarea pentru stratul curent
                    for n in range(self.dimHiddenLayers):
                        current_err = 0.0
                        for outErr_idx in range(len(output_error)):
                            current_err += self.coefs[back_idx][outErr_idx][n] * output_error[outErr_idx]
                        err.append(current_err)

                    errors.append(err)

                errors.append(output_error)
                # print(errors)

                #actualizarea coeficientilor
                for coef_idx in range(len(self.coefs)):
                    for w_idx in range(len(self.coefs[coef_idx])):
                        for n_idx in range(len(self.coefs[coef_idx][w_idx])):
                            self.coefs[coef_idx][w_idx][n_idx] += alpha * errors[coef_idx][w_idx] * neurons_inputs[coef_idx][w_idx]

                #print(self.coefs)

                probs.append(x)
                if(x[0] > x[1]):
                    computed.append(0)
                else:
                    computed.append(1)

            print("Loss: " + str(log_loss(outputs, probs)))


    def predict(self, inputs):
        computed = []
        for input_idx in range(len(inputs)):
            x = inputs[input_idx]
            for no_layer in range(len(self.coefs)):
                out = []
                for no_w in range(len(self.coefs[no_layer])):
                    value = 0.0
                    for w_idx in range(len(self.coefs[no_layer][no_w])):
                        value += x[w_idx] * self.coefs[no_layer][no_w][w_idx]
                    out.append(sigmoid(value))
                x = out

                # acum x-ul este ce scoate layer-ul de output si se face un softmax
            output_sum = sum(x)
            x = [nr / output_sum for nr in x]
            computed.append(0 if x[0] > x[1] else 1)

        return computed