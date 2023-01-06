##
## EPITECH PROJECT, 2022
## B-AIA-500-STG-5-1-gomoku-auguste.thomann
## File description:
## Makefile
##

NAME 	=	pbrain-gomoku-ai

all: $(NAME)
$(NAME):
	cp $(NAME).py $(NAME)
	chmod 764 $(NAME)

clean:
	@rm -rf __pycache__

fclean: clean
	@rm -f $(NAME)

re: fclean all

.PHONY: all clean fclean re