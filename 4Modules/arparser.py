import argparse
#basic usage with only help option
parser = argparse.ArgumentParser()
parser.parse_args()

#positional argument
parser = argparse.ArgumentParser()
parser.add_argument("echo",help="sample positional argument")
parser.parse_args()

#argparse treats the options we gave it as strings, until we explicitly mention it.
parser = argparse.ArgumentParser()
parser.add_argument("echo", help="sample positional argument",type = int)
args=parser.parse_args()
print(args.echo)

#optional parameters #optional parameters requires one argument by default.
parser = argparse.ArgumentParser()
parser.add_argument("--echo", help="sample optional argument")
args = parser.parse_args()
print(args.echo)

#making optional parameters to take no argument
#by default if an argument is not specified for optional parameter then it takes None value.
#action="store_true" simple tells mentioning of that option means set it to True
parser = argparse.ArgumentParser()
parser.add_argument("--echo", help="sample optional argument",action="store_true")
args = parser.parse_args()
print(args.echo)

#using short option for optional parameters
parser = argparse.ArgumentParser()
parser.add_argument("-e","--echo", help="sample optional argument with short option or one dashed option")
args = parser.parse_args()
print(args.echo)

#we can restirct the arguments using default, by specifing a list of allowed values for that parameter
parser = argparse.ArgumentParser()
parser.add_argument("--echo", help="sample optional argument",type=int,choices=[0,1,2])
args = parser.parse_args()
print(args.echo)

#by using action="count" we can count the no. of occurences of that option and behave accordingly.
parser = argparse.ArgumentParser()
parser.add_argument("-e","--echo", help="sample optional argument",action="count")
args = parser.parse_args()
print(args.echo)

#we can use default to set the default value of an optional parameter.
parser = argparse.ArgumentParser()
parser.add_argument("--echo", help="sample optional argument with default value",type=int,choices=[0,1,2],default=0)
args = parser.parse_args()
print(args.echo)

#mutually exclusive parameters.
parser = argparse.ArgumentParser()
group = parser.add_mutually_exclusive_group()
group.add_argument("echo", help="eccccchooo")
group.add_argument("quiet", help="quietttttt")
args = parser.parse_args()




