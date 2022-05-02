#include "stockholm.hpp"

static void	st_error(const std::string& error)
{
	std::cout << "Error: " << error << std::endl;
	exit(1);
}

static std::map<std::string, std::string>	st_create_tokens(char **input)
{
	int					count;
	std::string				current_val;
	std::map<std::string, std::string>	tokens;

	count = 0;
	while (input[count])
	{
		current_val = input[count];
		if (current_val == "-h" || current_val == "-help")
		{
			if (tokens.count("H"))
				st_error("(format) ./program [-hvrs]");
			tokens.insert(std::pair<std::string, std::string>("H", "0"));
		}
		else if (current_val == "-v" || current_val == "-version")
		{
			if (tokens.count("V"))
				st_error("(format) ./program [-hvrs]");
			tokens.insert(std::pair<std::string, std::string>("V", "0"));
		}
		else if (current_val == "-r" || current_val == "-reverse")
		{
			count++;
			if (tokens.count("R") || !input[count])
				st_error("(format) ./program [-hvrs]");
			tokens.insert(std::pair<std::string, std::string>("R", input[count]));
		}
		else if (current_val == "-s" || current_val == "-silent")
		{
			if (tokens.count("S"))
				st_error("(format) ./program [-hvrs]");
			tokens.insert(std::pair<std::string, std::string>("S", "0"));
		}
		else
			st_error("(format) ./program [-hvrs]");
		count++;
	}
	if ((tokens.count("H") || tokens.count("V")) && tokens.size() > 1) 
		st_error("(format) ./program [-hvrs]");
	return (tokens);
}

static int	st_execute_tokens(std::map<std::string, std::string> &tokens)
{
	std::string	help;
	std::string	version;
	std::string	reverse;
	std::string	key;
	std::string	silent;
	std::string	command;

	help = tokens.count("H") ? "H" : "0";
	version = tokens.count("V") ? "V" : "0";
	reverse = tokens.count("R") ? "R" : "0";
	key = tokens.count("R") ? tokens["R"] : "0";
	silent = tokens.count("S") ? "S" : "0";
	command = "python3 encrypt.py ";
	command += help + " ";
	command += version + " ";
	command += reverse + " ";
	command += silent + " ";
	command += key;
	system(command.c_str());
	return (0);
}

int			main(int argc, char *argv[])
{
	std::map<std::string, std::string>	tokens;

	(void)argc;
	tokens = st_create_tokens(argv + 1);
	if (st_execute_tokens(tokens))
		st_error("(exec) stockholm couldn't be executed");
	return (0);
}
