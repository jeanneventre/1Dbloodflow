objects= 	$(OBJ_DIR)/main.o $(OBJ_DIR)/network.o \
					$(OBJ_DIR)/artery.o $(OBJ_DIR)/arteryNum.o $(OBJ_DIR)/arteryBC.o \
					$(OBJ_DIR)/vesselProperties.o $(OBJ_DIR)/parser.o \
					$(OBJ_DIR)/matrix.o $(OBJ_DIR)/VECT.o $(OBJ_DIR)/triDiagMatrix.o \
					$(OBJ_DIR)/helpFunctions.o $(OBJ_DIR)/profile.o $(OBJ_DIR)/alger.o\
					$(OBJ_DIR)/file.o $(OBJ_DIR)/bc.o $(OBJ_DIR)/timenet.o $(OBJ_DIR)/output.o $(OBJ_DIR)/residu.o \
	 				$(OBJ_DIR)/stringManage.o $(OBJ_DIR)/error.o

INC_DIR=../include
SRC_DIR=../src
OBJ_DIR=obj

CXX= g++ # (use it instead of gcc because it assumes the c++ library by defautl)

CFLAGS=-I$(INC_DIR) -std=c++11 -Wall -Wextra -Wstrict-overflow=5 -Wunused-parameter -Wformat=2 -Wunknown-pragmas -O3 -D NDEBUG -fopenmp -pthread  # clang++ libc++ / g++ libstdc++

LDFLAGS= -fopenmp -pthread

all: multilayerLINUX

multilayerMAC: $(objects)
	$(CXX) $(LDFLAGS) -o bin/MAC/multilayerSingle $(objects)

$(OBJ_DIR)/main.o: ../main.cpp $(INC_DIR)/network.h
	$(CXX) -c -o $@ $< $(CFLAGS)

$(OBJ_DIR)/network.o:$(SRC_DIR)/network.cpp $(INC_DIR)/misc.h $(INC_DIR)/parser.h $(INC_DIR)/timenet.h $(INC_DIR)/output.h $(INC_DIR)/residu.h $(INC_DIR)/artery.h $(INC_DIR)/arteryNum.h
	$(CXX) -c -o $@ $< $(CFLAGS)

$(OBJ_DIR)/arteryNum.o: $(SRC_DIR)/arteryNum.cpp $(INC_DIR)/misc.h $(INC_DIR)/VECT.h $(INC_DIR)/bc.h $(INC_DIR)/timenet.h $(INC_DIR)/vesselProperties.h $(INC_DIR)/triDiagMatrix.h $(INC_DIR)/artery.h $(INC_DIR)/arteryBC.h $(INC_DIR)/helpFunctions.h $(INC_DIR)/alger.h
	$(CXX) -c -o $@ $< $(CFLAGS)

$(OBJ_DIR)/artery.o: $(SRC_DIR)/artery.cpp $(INC_DIR)/misc.h $(INC_DIR)/VECT.h $(INC_DIR)/bc.h $(INC_DIR)/timenet.h $(INC_DIR)/vesselProperties.h $(INC_DIR)/helpFunctions.h $(INC_DIR)/profile.h
	$(CXX) -c -o $@ $< $(CFLAGS)

$(OBJ_DIR)/arteryBC.o: $(SRC_DIR)/arteryBC.cpp $(INC_DIR)/misc.h $(INC_DIR)/VECT.h $(INC_DIR)/helpFunctions.h $(INC_DIR)/profile.h $(INC_DIR)/alger.h
	$(CXX) -c -o $@ $< $(CFLAGS)

$(OBJ_DIR)/parser.o: $(SRC_DIR)/parser.cpp $(INC_DIR)/misc.h $(INC_DIR)/vesselProperties.h $(INC_DIR)/stringManage.h $(INC_DIR)/file.h $(INC_DIR)/bc.h $(INC_DIR)/timenet.h $(INC_DIR)/output.h
	$(CXX) -c -o $@ $< $(CFLAGS)

$(OBJ_DIR)/vesselProperties.o: $(SRC_DIR)/vesselProperties.cpp $(INC_DIR)/misc.h $(INC_DIR)/VECT.h $(INC_DIR)/bc.h
	$(CXX) -c -o $@ $< $(CFLAGS)
$(OBJ_DIR)/triDiagMatrix.o:$(SRC_DIR)/triDiagMatrix.cpp $(INC_DIR)/misc.h $(INC_DIR)/VECT.h
	$(CXX) -c -o $@ $< $(CFLAGS)

$(OBJ_DIR)/helpFunctions.o:$(SRC_DIR)/helpFunctions.cpp $(INC_DIR)/misc.h $(INC_DIR)/VECT.h
	$(CXX) -c -o $@ $< $(CFLAGS)
$(OBJ_DIR)/profile.o:$(SRC_DIR)/profile.cpp $(INC_DIR)/misc.h $(INC_DIR)/VECT.h $(INC_DIR)/error.h
	$(CXX) -c -o $@ $< $(CFLAGS)
$(OBJ_DIR)/alger.o:$(SRC_DIR)/alger.cpp $(INC_DIR)/misc.h $(INC_DIR)/VECT.h
	$(CXX) -c -o $@ $< $(CFLAGS)

$(OBJ_DIR)/timenet.o:$(SRC_DIR)/timenet.cpp $(INC_DIR)/misc.h $(INC_DIR)/VECT.h
	$(CXX) -c -o $@ $< $(CFLAGS)
$(OBJ_DIR)/bc.o:$(SRC_DIR)/bc.cpp $(INC_DIR)/misc.h $(INC_DIR)/VECT.h
	$(CXX) -c -o $@ $< $(CFLAGS)

$(OBJ_DIR)/residu.o:$(SRC_DIR)/residu.cpp $(INC_DIR)/misc.h
	$(CXX) -c -o $@ $< $(CFLAGS)
$(OBJ_DIR)/output.o:$(SRC_DIR)/output.cpp $(INC_DIR)/misc.h
	$(CXX) -c -o $@ $< $(CFLAGS)

$(OBJ_DIR)/file.o:$(SRC_DIR)/file.cpp $(INC_DIR)/misc.h
	$(CXX) -c -o $@ $< $(CFLAGS)
$(OBJ_DIR)/VECT.o: $(SRC_DIR)/VECT.cpp $(INC_DIR)/misc.h
	$(CXX) -c -o $@ $< $(CFLAGS)

$(OBJ_DIR)/matrix.o:$(SRC_DIR)/matrix.cpp $(INC_DIR)/lib.h
	$(CXX) -c -o $@ $< $(CFLAGS)
$(OBJ_DIR)/stringManage.o:$(SRC_DIR)/stringManage.cpp $(INC_DIR)/lib.h
	$(CXX) -c -o $@ $< $(CFLAGS)
$(OBJ_DIR)/error.o:$(SRC_DIR)/error.cpp $(INC_DIR)/lib.h
	$(CXX) -c -o $@ $< $(CFLAGS)


multilayerLINUX: $(objects)
	$(CXX) $(LDFLAGS) -o bin/LINUX/multilayerSingle $(objects)

$(OBJ_DIR)/main.o: ../main.cpp $(INC_DIR)/network.h
	$(CXX) -c -o $@ $< $(CFLAGS)

$(OBJ_DIR)/network.o:$(SRC_DIR)/network.cpp $(INC_DIR)/misc.h $(INC_DIR)/parser.h $(INC_DIR)/timenet.h $(INC_DIR)/output.h $(INC_DIR)/residu.h $(INC_DIR)/artery.h $(INC_DIR)/arteryNum.h
	$(CXX) -c -o $@ $< $(CFLAGS)

$(OBJ_DIR)/arteryNum.o: $(SRC_DIR)/arteryNum.cpp $(INC_DIR)/misc.h $(INC_DIR)/VECT.h $(INC_DIR)/bc.h $(INC_DIR)/timenet.h $(INC_DIR)/vesselProperties.h $(INC_DIR)/triDiagMatrix.h $(INC_DIR)/artery.h $(INC_DIR)/arteryBC.h $(INC_DIR)/helpFunctions.h $(INC_DIR)/alger.h
	$(CXX) -c -o $@ $< $(CFLAGS)

$(OBJ_DIR)/artery.o: $(SRC_DIR)/artery.cpp $(INC_DIR)/misc.h $(INC_DIR)/VECT.h $(INC_DIR)/bc.h $(INC_DIR)/timenet.h $(INC_DIR)/vesselProperties.h $(INC_DIR)/helpFunctions.h $(INC_DIR)/profile.h
	$(CXX) -c -o $@ $< $(CFLAGS)

$(OBJ_DIR)/arteryBC.o: $(SRC_DIR)/arteryBC.cpp $(INC_DIR)/misc.h $(INC_DIR)/VECT.h $(INC_DIR)/helpFunctions.h $(INC_DIR)/profile.h $(INC_DIR)/alger.h
	$(CXX) -c -o $@ $< $(CFLAGS)

$(OBJ_DIR)/parser.o: $(SRC_DIR)/parser.cpp $(INC_DIR)/misc.h $(INC_DIR)/vesselProperties.h $(INC_DIR)/stringManage.h $(INC_DIR)/file.h $(INC_DIR)/bc.h $(INC_DIR)/timenet.h $(INC_DIR)/output.h
	$(CXX) -c -o $@ $< $(CFLAGS)

$(OBJ_DIR)/vesselProperties.o: $(SRC_DIR)/vesselProperties.cpp $(INC_DIR)/misc.h $(INC_DIR)/VECT.h $(INC_DIR)/bc.h
	$(CXX) -c -o $@ $< $(CFLAGS)
$(OBJ_DIR)/triDiagMatrix.o:$(SRC_DIR)/triDiagMatrix.cpp $(INC_DIR)/misc.h $(INC_DIR)/VECT.h
	$(CXX) -c -o $@ $< $(CFLAGS)

$(OBJ_DIR)/helpFunctions.o:$(SRC_DIR)/helpFunctions.cpp $(INC_DIR)/misc.h $(INC_DIR)/VECT.h
	$(CXX) -c -o $@ $< $(CFLAGS)
$(OBJ_DIR)/profile.o:$(SRC_DIR)/profile.cpp $(INC_DIR)/misc.h $(INC_DIR)/VECT.h $(INC_DIR)/error.h
	$(CXX) -c -o $@ $< $(CFLAGS)
$(OBJ_DIR)/alger.o:$(SRC_DIR)/alger.cpp $(INC_DIR)/misc.h $(INC_DIR)/VECT.h
	$(CXX) -c -o $@ $< $(CFLAGS)

$(OBJ_DIR)/timenet.o:$(SRC_DIR)/timenet.cpp $(INC_DIR)/misc.h $(INC_DIR)/VECT.h
	$(CXX) -c -o $@ $< $(CFLAGS)
$(OBJ_DIR)/bc.o:$(SRC_DIR)/bc.cpp $(INC_DIR)/misc.h $(INC_DIR)/VECT.h
	$(CXX) -c -o $@ $< $(CFLAGS)

$(OBJ_DIR)/residu.o:$(SRC_DIR)/residu.cpp $(INC_DIR)/misc.h
	$(CXX) -c -o $@ $< $(CFLAGS)
$(OBJ_DIR)/output.o:$(SRC_DIR)/output.cpp $(INC_DIR)/misc.h
	$(CXX) -c -o $@ $< $(CFLAGS)

$(OBJ_DIR)/file.o:$(SRC_DIR)/file.cpp $(INC_DIR)/misc.h
	$(CXX) -c -o $@ $< $(CFLAGS)
$(OBJ_DIR)/VECT.o: $(SRC_DIR)/VECT.cpp $(INC_DIR)/misc.h
	$(CXX) -c -o $@ $< $(CFLAGS)

$(OBJ_DIR)/matrix.o:$(SRC_DIR)/matrix.cpp $(INC_DIR)/lib.h
	$(CXX) -c -o $@ $< $(CFLAGS)
$(OBJ_DIR)/stringManage.o:$(SRC_DIR)/stringManage.cpp $(INC_DIR)/lib.h
	$(CXX) -c -o $@ $< $(CFLAGS)
$(OBJ_DIR)/error.o:$(SRC_DIR)/error.cpp $(INC_DIR)/lib.h
	$(CXX) -c -o $@ $< $(CFLAGS)

cleanMAC:
	rm -rf $(OBJ_DIR)/*.o bin/MAC/multilayerSingle

cleanLINUX:
	rm -rf $(OBJ_DIR)/*.o bin/LINUX/multilayerSingle
