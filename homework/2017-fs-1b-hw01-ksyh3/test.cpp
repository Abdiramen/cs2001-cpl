// -*- mode: cpp -*-

#define BOOST_TEST_DYN_LINK
#define BOOST_TEST_MODULE DecryptorTest
#include <boost/test/unit_test.hpp>
#include "rotor.h"
#include "funcs.h"
#include <map>

/*
 * Test that a Rotor will decrypt letters correctly when using disk 1
 */
char alphabet[26] = {
  'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 
  'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
};

/*
 * Test that a Rotor will decrypt letters correctly when using disk 1
 */
BOOST_AUTO_TEST_CASE(test_disk1)
{
  /*
   * Iterating over the alphabet to ensure that the disk 1 produces the
   * individual correct response.
   */
  for(unsigned int i=0; i < sizeof(alphabet); i++)
  {
    Rotor rotor_1(1);
    BOOST_CHECK_EQUAL(
      rotor_1.decrypt(alphabet[i]), 
      static_cast<char>((((alphabet[i]) + 3) % 26) + 65)
    );
  }

  /*
   * Running a test string over the disk 1 to ensure a proper continous output
   */
  Rotor rotor_1(1);
  string decrypt_string = "KBLCMDNEOFPGQHRISJTKULVMWN";
  string translation_string = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
  for(unsigned int i=0; i < decrypt_string.length(); i++)
  {
    BOOST_CHECK_EQUAL(
      rotor_1.decrypt(decrypt_string[i]),
      translation_string[i]
    );
  }
}


/*
 * Test that a Rotor will decrypt letters correctly when using disk 2
 */
BOOST_AUTO_TEST_CASE(test_disk2)
{
  /*
   * Iterating over the alphabet to ensure that the disk 2 produces the
   * individual correct response.
   */
  for(unsigned int i=0; i < sizeof(alphabet); i++)
  {
    Rotor rotor_1(2);
    BOOST_CHECK_EQUAL(
      rotor_1.decrypt(alphabet[i]), 
      static_cast<char>((((alphabet[i]) + 5) % 26) + 65)
    );
  }

  /*
   * Running a test string over the disk 2 to ensure a proper continous output
   */
  Rotor rotor_1(2);
  string decrypt_string = "IBJCKDLEMFNGOHPIQJRKSLTMUN";
  string translation_string = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
  for(unsigned int i=0; i < decrypt_string.length(); i++)
  {
    BOOST_CHECK_EQUAL(
      rotor_1.decrypt(decrypt_string[i]),
      translation_string[i]
    );
  }

}

/*
 * Test that a Rotor will decrypt letters correctly when using disk 3
 */
BOOST_AUTO_TEST_CASE(test_disk3)
{
  /*
   * Creating a map which maps the translation of each individual character
   * in the disk 3
   */
	map<char, char> pair_map;
	pair_map['A'] = 'Y';
	pair_map['B'] = 'J';
	pair_map['C'] = 'T';
	pair_map['D'] = 'Z';
	pair_map['E'] = 'O';
	pair_map['F'] = 'G';
	pair_map['G'] = 'C';
	pair_map['H'] = 'L';
	pair_map['I'] = 'M';
	pair_map['J'] = 'A';
	pair_map['K'] = 'E';
	pair_map['L'] = 'K';
	pair_map['M'] = 'U';
	pair_map['N'] = 'H';
	pair_map['O'] = 'P';
	pair_map['P'] = 'X';
	pair_map['Q'] = 'S';
	pair_map['R'] = 'F';
	pair_map['S'] = 'W';
	pair_map['T'] = 'B';
	pair_map['U'] = 'D';
	pair_map['V'] = 'Q';
	pair_map['W'] = 'N';
	pair_map['X'] = 'V';
	pair_map['Y'] = 'R';
	pair_map['Z'] = 'I';

  /*
   * Iterating over the alphabet to ensure that the disk 3 produces the
   * individual correct response.
   */
	for(unsigned int i=0; i < sizeof(alphabet); i++)
  {
    Rotor rotor_1(3);
    BOOST_CHECK_EQUAL(
      rotor_1.decrypt(alphabet[i]), 
			pair_map[alphabet[i]]
    );
  }

  /*
   * Running a test string over the disk 3 to ensure a proper continous output
   */
  Rotor rotor_1(3);
  string decrypt_string = "JKWYMFANMPWLXZFJMMEYOJJGUJ";
  string translation_string = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
  for(unsigned int i=0; i < decrypt_string.length(); i++)
  {
    BOOST_CHECK_EQUAL(
      rotor_1.decrypt(decrypt_string[i]),
      translation_string[i]
    );
  }
}

/*
 * Test that a Rotor will decrypt letters correctly when using disk 4
 */
BOOST_AUTO_TEST_CASE(test_disk4)
{
  /*
   * Iterating over the alphabet to ensure that the disk 4 produces the
   * individual correct response.
   */

  for(unsigned int i=0; i < sizeof(alphabet); i++)
  {
    Rotor rotor_1(4);
    if(alphabet[i] % 2 == 0)
    {
      BOOST_CHECK_EQUAL(
        rotor_1.decrypt(alphabet[i]), 
        static_cast<char>(alphabet[i] - 1)
      );
    }
    else
    {
      BOOST_CHECK_EQUAL(
        rotor_1.decrypt(alphabet[i]), 
        static_cast<char>(alphabet[i] + 1)
      );
    }
  }

  /*
   * Running a test string over the disk 4 to ensure a proper continous output
   */
  Rotor rotor_1(4);
  string decrypt_string = "BZEYHXKWNVQUTTWSZRCQFPIOLN";
  string translation_string = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
  for(unsigned int i=0; i < decrypt_string.length(); i++)
  {
    BOOST_CHECK_EQUAL(
      rotor_1.decrypt(decrypt_string[i]),
      translation_string[i]
    );
  }
}

/**
 * Test that a Rotor will decrypt letters correctly when using disk 5
 */
BOOST_AUTO_TEST_CASE(test_disk5)
{
  /*
   * Iterating over the alphabet to ensure that the disk 5 produces the
   * individual correct response.
   */
  for(unsigned int i=0; i < sizeof(alphabet); i++)
  {
    Rotor rotor_1(5);
    BOOST_CHECK_EQUAL(
      rotor_1.decrypt(alphabet[i]), 
      static_cast<char>((alphabet[i]) + (25 - 2 * i))
    );
  }

  /*
   * Running a test string over the disk 5 to ensure a proper continous output
   */
  Rotor rotor_1(5);
  const string decrypt_string = "ZZYYXXWWVVUUTTSSRRQQPPOONN";
  const string translation_string = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
  for(unsigned int i=0; i < decrypt_string.length(); i++)
  {
    BOOST_CHECK_EQUAL(
      rotor_1.decrypt(decrypt_string[i]),
      translation_string[i]
    );
  }
}

BOOST_AUTO_TEST_CASE(test_decrypt_message)
{
  const string message = "THE_QUICK_BROWN_FOX_JUMPS_OVER_THE_LAZY_DOG";
  /*
   * Checking the test message for disk combination 1,2,3 produces the message.
   */
  BOOST_CHECK_EQUAL(
    decrypt_message(1, 2, 3, "UZJ_HVOCY_JFUQR_GBH_BRDJT_ZQCB_HRT_ARPM_EXU"),
    message
  );

  /*
   * Checking the test message for disk combination 1,2,4 produces the message.
   */
  BOOST_CHECK_EQUAL(
    decrypt_message(1, 2, 4, "KWR_YKYLE_NKYQQ_SFT_APFKP_RWHU_XEM_VGND_ELP"),
    message
  );

  /*
   * Checking the test message for disk combination 1,2,5 produces the message.
   */
  BOOST_CHECK_EQUAL(
    decrypt_message(1, 2, 5, "YSD_EWSHA_PMMYA_SPL_CHFCJ_DWTQ_NUO_HYBB_WXR"),
    message
  );

}
